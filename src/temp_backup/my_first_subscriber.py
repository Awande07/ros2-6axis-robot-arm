#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyFirstSubscriber(Node):
    def __init__(self):
        super().__init__('my_first_subscriber')
        print("Subscriber started! Waiting for messages...")
        self.subscription = self.create_subscription(
            String,
            'greetings',
            self.listener_callback,
            10
        )
        
    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        print(f"📨 Received: {msg.data}")  # This will definitely show

def main(args=None):
    rclpy.init(args=args)
    my_first_subscriber = MyFirstSubscriber()
    print("Subscriber node is running...")
    try:
        rclpy.spin(my_first_subscriber)
    except KeyboardInterrupt:
        print("\nShutting down subscriber...")
    finally:
        my_first_subscriber.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
