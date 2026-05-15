#!/usr/bin/env python3

import rclpy
import time
from rclpy.node import Node
from rclpy.action import ActionServer
from ros2_advanced.action import MoveArm

class ArmActionServer(Node):
    def __init__(self):
        super().__init__('arm_action_server')
        
        # Create the action server
        self.action_server = ActionServer(
            self,
            MoveArm,
            'move_arm',
            self.execute_callback
        )
        
        self.get_logger().info('Arm Action Server is ready!')
        
    def execute_callback(self, goal_handle):
        """This function runs when a client sends a goal."""
        
        # Get the goal from the client
        target_positions = goal_handle.request.target_positions
        max_duration = goal_handle.request.max_duration_seconds
        
        self.get_logger().info(f'Received goal: move to {target_positions}')
        
        # Initialize current positions (starting at 0 for all joints)
        current_positions = [0.0] * len(target_positions)
        
        # Simulate moving the arm
        steps = 20  # Number of feedback messages to send
        step_duration = min(max_duration / steps, 0.1)  # Use 0.1s max per step
        
        for i in range(steps + 1):
            # Calculate percentage complete
            percentage = (i / steps) * 100.0
            
            # Update current positions linearly from 0 to target
            for j in range(len(target_positions)):
                current_positions[j] = (percentage / 100.0) * target_positions[j]
            
            # Create feedback message
            feedback_msg = MoveArm.Feedback()
            feedback_msg.current_positions = current_positions
            feedback_msg.percentage_complete = percentage
            feedback_msg.status_message = f'Moving to target... {percentage:.1f}% complete'
            
            # Publish feedback
            goal_handle.publish_feedback(feedback_msg)
            self.get_logger().info(f'Feedback: {percentage:.0f}% - Positions: {[round(p,2) for p in current_positions]}')
            
            # Check if the goal was canceled
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().warn('Goal was canceled!')
                
                # Return canceled result
                result = MoveArm.Result()
                result.success = False
                result.message = 'Movement canceled by user'
                result.total_duration = time.time() - goal_handle.request_started_at
                return result
            
            # Wait before next feedback
            time.sleep(step_duration)
        
        # Goal completed successfully
        goal_handle.succeed()
        
        # Create result message
        result = MoveArm.Result()
        result.success = True
        result.message = 'Arm moved successfully to target position'
        result.total_duration = time.time() - goal_handle.request_started_at
        
        self.get_logger().info(f'Result: Arm movement complete in {result.total_duration:.2f} seconds')
        
        return result

def main(args=None):
    rclpy.init(args=args)
    node = ArmActionServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()