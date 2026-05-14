import os
from glob import glob
from setuptools import setup, find_packages

package_name = 'ros2_advanced'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
            data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), 
         glob(os.path.join('launch', '*.launch.py'))),
        (os.path.join('share', package_name, 'urdf'), 
         glob(os.path.join('urdf', '*.urdf'))),
        (os.path.join('share', package_name, 'config'), 
         glob(os.path.join('config', '*.rviz'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Awande',
    maintainer_email='awandelindani07@gmail.com',
    description='Advanced ROS 2 package for Chapters 5-18',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = ros2_advanced.publisher_node:main',
            'subscriber = ros2_advanced.subscriber_node:main',
            'tf_broadcaster = ros2_advanced.tf_broadcaster:main',
            'tf_listener = ros2_advanced.tf_listener:main',
        ],
    },
)