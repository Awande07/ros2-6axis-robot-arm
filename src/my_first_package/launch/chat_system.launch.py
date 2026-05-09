#!/usr/bin/env python3
# This is a ROS 2 launch file. It uses Python syntax.

# Import the LaunchDescription class and action modules
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    """This function returns a LaunchDescription containing all nodes to start."""
    
    # Define the first node: your publisher from Chapter 2
    publisher_node = Node(
        package='my_first_package',           # Which package has this node
        executable='my_first_node',           # Which executable to run
        name='chat_publisher',                # Give it a custom name (optional)
        output='screen',                      # Print output to the terminal
    )
    
    # Define the second node: your subscriber from Chapter 2
    subscriber_node = Node(
        package='my_first_package',
        executable='my_first_subscriber',
        name='chat_subscriber',
        output='screen',
    )
    
    # Create and return the LaunchDescription containing both nodes
    return LaunchDescription([
        publisher_node,
        subscriber_node,
    ])