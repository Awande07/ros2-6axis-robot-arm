#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

class TFListener(Node):
    def __init__(self):
        super().__init__('tf_listener')
        
        # Create a buffer to store transforms
        self.tf_buffer = Buffer()
        
        # Create a listener that fills the buffer
        self.tf_listener = TransformListener(self.tf_buffer, self)
        
        # Create a timer to check the transform every 0.5 seconds
        self.timer = self.create_timer(0.5, self.query_transform)
        
        self.get_logger().info('TF Listener started!')
        
    def query_transform(self):
        try:
            # Look up the transform from base_link to camera_link
            # Parameters: target_frame, source_frame, time
            transform = self.tf_buffer.lookup_transform(
                'base_link',      # Target frame (what we want to know position relative to)
                'camera_link',    # Source frame (what we want to know position of)
                rclpy.time.Time() # Current time
            )
            
            # Extract translation (position)
            x = transform.transform.translation.x
            y = transform.transform.translation.y
            z = transform.transform.translation.z
            
            self.get_logger().info(f'Camera is at: x={x:.2f}, y={y:.2f}, z={z:.2f} relative to base')
            
        except TransformException as e:
            # This happens if the transform hasn't been broadcast yet
            self.get_logger().warn(f'Transform not available: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = TFListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()