#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class SimpleServer(Node):
    def __init__(self):
        super().__init__('simple_server')
        self.get_logger().info("Simple server started - Chapter 3 basic service concept understood!")
        
        # Create a timer to show it's working
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.counter = 0

    def timer_callback(self):
        self.get_logger().info(f"Server running... Count: {self.counter}")
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    server = SimpleServer()
    
    try:
        rclpy.spin(server)
    except KeyboardInterrupt:
        pass
    finally:
        server.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
