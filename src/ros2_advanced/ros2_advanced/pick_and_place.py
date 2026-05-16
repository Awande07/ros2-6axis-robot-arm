#!/usr/bin/env python3
"""Simplified pick and place using joint goals - WORKS with Humble"""

import rclpy
import time
from rclpy.node import Node
from rclpy.action import ActionClient
from moveit_msgs.action import MoveGroup
from moveit_msgs.msg import Constraints, JointConstraint

class PickAndPlace(Node):
    def __init__(self):
        super().__init__('pick_and_place')
        self.action_client = ActionClient(self, MoveGroup, 'move_action')
        self.get_logger().info('Pick and Place node ready!')
        
    def wait_for_server(self):
        self.get_logger().info('Waiting for MoveIt server...')
        self.action_client.wait_for_server()
        self.get_logger().info('Connected to MoveIt server!')
        
    def send_joint_goal(self, joint_positions, name="goal"):
        """Send a joint position goal."""
        goal_msg = MoveGroup.Goal()
        
        # Set workspace bounds (simple)
        goal_msg.request.workspace_parameters.min_corner.x = -2.0
        goal_msg.request.workspace_parameters.min_corner.y = -2.0
        goal_msg.request.workspace_parameters.min_corner.z = -2.0
        goal_msg.request.workspace_parameters.max_corner.x = 2.0
        goal_msg.request.workspace_parameters.max_corner.y = 2.0
        goal_msg.request.workspace_parameters.max_corner.z = 2.0
        
        # Create constraints for each joint
        constraints = Constraints()
        constraints.name = name
        
        joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
        
        for i, (joint_name, position) in enumerate(zip(joint_names, joint_positions)):
            jc = JointConstraint()
            jc.joint_name = joint_name
            jc.position = position
            jc.tolerance_above = 0.01
            jc.tolerance_below = 0.01
            jc.weight = 1.0
            constraints.joint_constraints.append(jc)
        
        goal_msg.request.goal_constraints.append(constraints)
        
        self.get_logger().info(f'Sending goal: {name}')
        future = self.action_client.send_goal_async(goal_msg)
        future.add_done_callback(self.goal_response_callback)
        return future
        
    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().error('Goal rejected!')
            return
        self.get_logger().info('Goal accepted, waiting for result...')
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.result_callback)
        
    def result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'Movement complete!')
        
    def pick_and_place_sequence(self):
        self.wait_for_server()
        
        # Define joint position sets (in radians)
        positions = [
            ([0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "home"),
            ([1.0, 0.5, 0.0, 0.0, 0.0, 0.0], "reach_forward"),
            ([1.0, 0.5, 0.3, 0.0, 0.0, 0.0], "pick_position"),
            ([1.0, 0.5, 0.3, 0.5, 0.0, 0.0], "rotate_wrist"),
            ([0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "return_home"),
        ]
        
        for joints, name in positions:
            self.send_joint_goal(joints, name)
            time.sleep(3.0)  # Wait for each movement
            
        self.get_logger().info('Pick and place sequence complete!')
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = PickAndPlace()
    node.pick_and_place_sequence()
    rclpy.spin(node)

if __name__ == '__main__':
    main()