#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import random

class RobotMonitor(Node):
    def __init__(self):
        super().__init__('robot_monitor')
        
        # Declare parameters with default values
        self.declare_parameter('robot_name', 'DefaultRobot')
        self.declare_parameter('max_cpu_temperature', 85.0)
        self.declare_parameter('publish_rate', 1.0)  # Hz
        self.declare_parameter('is_verbose', False)
        
        # Get parameter values
        self.robot_name = self.get_parameter('robot_name').value
        self.max_temp = self.get_parameter('max_cpu_temperature').value
        self.publish_rate = self.get_parameter('publish_rate').value
        self.is_verbose = self.get_parameter('is_verbose').value
        
        # Create timer based on publish_rate parameter
        timer_period = 1.0 / self.publish_rate
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        # Log startup info
        self.get_logger().info(f'Robot Monitor started for: {self.robot_name}')
        self.get_logger().info(f'Max CPU Temperature: {self.max_temp}°C')
        self.get_logger().info(f'Publish Rate: {self.publish_rate} Hz')
        self.get_logger().info(f'Verbose Mode: {self.is_verbose}')
        
        # Add parameter change callback
        self.add_on_set_parameters_callback(self.parameter_change_callback)

    def parameter_change_callback(self, params):
        """Handle parameter changes at runtime"""
        for param in params:
            if param.name == 'robot_name':
                self.robot_name = param.value
                self.get_logger().info(f'Robot name changed to: {self.robot_name}')
            elif param.name == 'max_cpu_temperature':
                self.max_temp = param.value
                self.get_logger().info(f'Max temperature changed to: {self.max_temp}°C')
            elif param.name == 'publish_rate':
                self.publish_rate = param.value
                # Update timer period
                self.timer.cancel()
                timer_period = 1.0 / self.publish_rate
                self.timer = self.create_timer(timer_period, self.timer_callback)
                self.get_logger().info(f'Publish rate changed to: {self.publish_rate} Hz')
            elif param.name == 'is_verbose':
                self.is_verbose = param.value
                self.get_logger().info(f'Verbose mode changed to: {self.is_verbose}')
        
        return rclpy.node.SetParametersResult(successful=True)

    def timer_callback(self):
        """Simulate monitoring robot CPU temperature"""
        # Simulate CPU temperature (random between 70 and 90)
        cpu_temp = random.uniform(70.0, 90.0)
        
        # Check if temperature exceeds threshold
        if cpu_temp > self.max_temp:
            self.get_logger().warn(
                f'[{self.robot_name}] WARNING: CPU temperature {cpu_temp:.1f}°C '
                f'exceeds threshold {self.max_temp}°C!'
            )
        
        # Log verbose info if enabled
        elif self.is_verbose:
            self.get_logger().info(
                f'[{self.robot_name}] CPU temperature: {cpu_temp:.1f}°C '
                f'(Threshold: {self.max_temp}°C)'
            )

def main(args=None):
    rclpy.init(args=args)
    node = RobotMonitor()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
