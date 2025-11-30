#!/usr/bin/env python3

import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class StdServiceClient(Node):
    def __init__(self):
        super().__init__('std_service_client')
        self.client = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')
        self.get_logger().info("Service found!")

    def send_request(self, a, b):
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        self.future = self.client.call_async(request)
        return self.future

def main(args=None):
    rclpy.init(args=args)
    
    if len(sys.argv) != 3:
        print("Usage: use_std_client <a> <b>")
        return 1
    
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    
    client = StdServiceClient()
    future = client.send_request(a, b)
    
    while rclpy.ok():
        rclpy.spin_once(client)
        if future.done():
            try:
                response = future.result()
            except Exception as e:
                client.get_logger().error(f'Service call failed: {e}')
            else:
                client.get_logger().info(f"Result: {a} + {b} = {response.sum}")
            break
    
    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
