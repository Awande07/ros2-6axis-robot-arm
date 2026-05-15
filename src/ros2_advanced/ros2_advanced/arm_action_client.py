#!/usr/bin/env python3

import rclpy
import sys
from rclpy.node import Node
from rclpy.action import ActionClient
from ros2_advanced.action import MoveArm

class ArmActionClient(Node):
    def __init__(self):
        super().__init__('arm_action_client')
        self.action_client = ActionClient(self, MoveArm, 'move_arm')
        self.get_logger().info('Arm Action Client ready!')
        
    def send_goal(self, target_positions, max_duration=5.0):
        """Send a goal to the action server."""
        
        # Create goal message
        goal_msg = MoveArm.Goal()
        goal_msg.target_positions = target_positions
        goal_msg.max_duration_seconds = max_duration
        
        self.get_logger().info(f'Sending goal: move to {target_positions}')
        
        # Wait for the server to be available
        self.action_client.wait_for_server()
        
        # Send the goal
        self.send_goal_future = self.action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        
        # Add a callback for when the goal is accepted
        self.send_goal_future.add_done_callback(self.goal_response_callback)
        
    def goal_response_callback(self, future):
        """Called when the server responds to our goal request."""
        
        goal_handle = future.result()
        
        if not goal_handle.accepted:
            self.get_logger().error('Goal was rejected!')
            return
            
        self.get_logger().info('Goal accepted, waiting for result...')
        
        # Get the result
        self.get_result_future = goal_handle.get_result_async()
        self.get_result_future.add_done_callback(self.result_callback)
        
    def feedback_callback(self, feedback_msg):
        """Called whenever the server publishes feedback."""
        
        feedback = feedback_msg.feedback
        self.get_logger().info(
            f'Feedback: {feedback.percentage_complete:.0f}% - '
            f'{feedback.status_message}'
        )
        
    def result_callback(self, future):
        """Called when the action completes."""
        
        result = future.result().result
        status = future.result().status
        
        if result.success:
            self.get_logger().info(f'SUCCESS! {result.message}')
            self.get_logger().info(f'Total duration: {result.total_duration:.2f} seconds')
        else:
            self.get_logger().error(f'FAILED! {result.message}')
            
        # Shutdown after completion
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    
    # Parse command line arguments
    # Example: ros2 run ros2_advanced arm_action_client "1.0 0.5 0.2"
    if len(sys.argv) < 2:
        print("Usage: arm_action_client 'joint1 joint2 joint3'")
        print("Example: arm_action_client '1.57 0.78 0.0'")
        return
        
    # Parse target positions from command line
    target_positions = [float(x) for x in sys.argv[1].split()]
    
    client = ArmActionClient()
    client.send_goal(target_positions)
    
    # Keep spinning until shutdown
    rclpy.spin(client)

if __name__ == '__main__':
    main()