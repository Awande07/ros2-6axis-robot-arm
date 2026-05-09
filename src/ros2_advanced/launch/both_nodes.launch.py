#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_advanced',
            executable='publisher',
            name='publisher_node',
            output='screen',
        ),
        Node(
            package='ros2_advanced',
            executable='subscriber',
            name='subscriber_node',
            output='screen',
        ),
    ])