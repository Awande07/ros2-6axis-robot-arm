#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration
import os

def generate_launch_description():
    # Path to the URDF file
    urdf_file = '/workspaces/ros2_ws/src/ros2_advanced/urdf/two_link_arm.urdf'
    
    # Read the URDF file as a string
    with open(urdf_file, 'r') as f:
        robot_description = f.read()
    
    return LaunchDescription([
        # Node: robot_state_publisher (reads URDF and publishes transforms)
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description}]
        ),
        
        # Node: joint_state_publisher_gui (allows you to move joints with sliders)
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        ),
        
        # Node: RViz (visualization)
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', '/workspaces/ros2_ws/src/ros2_advanced/config/basic_rviz.rviz']
        )
    ])