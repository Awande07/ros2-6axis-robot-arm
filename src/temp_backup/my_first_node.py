#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyFirstNode(Node):
    def __init__(self):
        super().__init__('my_first_node')
        self.publisher_ = self.create_publisher(String, 'greetings', 10)

def main(args=None):
    rclpy.init(args=args)
    my_first_node = MyFirstNode()
    
    # Interactive chat loop
    try:
        print("--- My Simple ROS Chat ---")
        print("Type your message and press Enter. Type 'quit' to exit.")
        while rclpy.ok():
            # Get input from the user
            user_input = input("You: ")
            
            # Check if the user wants to quit
            if user_input.lower() == 'quit':
                break
                
            # Create and publish the message
            msg = String()
            msg.data = user_input
            my_first_node.publisher_.publish(msg)
            my_first_node.get_logger().info('Publishing: "%s"' % msg.data)
            
    except KeyboardInterrupt:
        print("\nShutting down publisher...")
    finally:
        my_first_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
