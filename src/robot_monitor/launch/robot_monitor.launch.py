from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_monitor',
            executable='robot_monitor_node',
            name='robot_monitor',
            parameters=[
                {'robot_name': 'ABB_Robot'},
                {'max_cpu_temperature': 80.0},
                {'publish_rate': 1.0},
                {'is_verbose': False}
            ]
        )
    ])
