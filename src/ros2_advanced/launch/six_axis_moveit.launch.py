#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    # Paths
    urdf_file = '/workspaces/ros2_ws/src/ros2_advanced/urdf/six_axis_arm.urdf'
    srdf_file = '/workspaces/ros2_ws/src/ros2_advanced/config/six_axis_arm.srdf'
    
    # Read files
    with open(urdf_file, 'r') as f:
        robot_description = f.read()
    
    with open(srdf_file, 'r') as f:
        robot_description_semantic = f.read()
    
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description}]
        ),
        
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': True}]
        ),
        
        Node(
            package='moveit_ros_move_group',
            executable='move_group',
            name='move_group',
            output='screen',
            parameters=[{
                'robot_description': robot_description,
                'robot_description_semantic': robot_description_semantic,
                'use_sim_time': True
            }]
        ),
    ])