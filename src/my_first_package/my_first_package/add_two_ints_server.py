#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_first_package.srv import AddTwoInts

class AddTwoIntsServer(Node):
    def __init__(self):
        super().__init__('add_two_ints_server')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.handle_add_two_ints)
        self.get_logger().info("Service server ready. Waiting for requests...")

    def handle_add_two_ints(self, request, response):
        self.get_logger().info(f"Incoming request: {request.a} + {request.b}")
        response.sum = request.a + request.b
        self.get_logger().info(f"Sending response: {response.sum}")
        return response

def main(args=None):
    rclpy.init(args=args)
    server = AddTwoIntsServer()
    rclpy.spin(server)
    server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()