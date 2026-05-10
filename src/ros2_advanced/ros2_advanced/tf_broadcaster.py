#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster
import math

class TFBroadcaster(Node):
    def __init__(self):
        super().__init__('tf_broadcaster')
        
        # Create a broadcaster object
        self.tf_broadcaster = TransformBroadcaster(self)
        
        # Create a timer to broadcast transforms at 10 Hz
        self.timer = self.create_timer(0.1, self.broadcast_tf)
        
        self.get_logger().info('TF Broadcaster started!')
    def broadcast_tf(self):
        t = TransformStamped()
        
        t.header.frame_id = 'base_link'
        t.child_frame_id = 'camera_link'
        t.header.stamp = self.get_clock().now().to_msg()
        
        # Make the camera move back and forth in a sine wave
        # Get current time in seconds
        current_time = self.get_clock().now().seconds_nanoseconds()[0]
        
        # Oscillating x position between 0.3 and 0.7 meters
        x_position = 0.5 + 0.2 * math.sin(current_time)
        
        t.transform.translation.x = x_position
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.2
        
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0
        
        self.tf_broadcaster.sendTransform(t)
        
        if int(current_time) % 5 == 0:
            self.get_logger().info(f'Broadcasting: camera at x={x_position:.2f}')
            
def main(args=None):
    rclpy.init(args=args)
    node = TFBroadcaster()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()