from setuptools import setup, find_packages

package_name = 'my_first_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Awande',
    maintainer_email='awandelindani07@gmail.com',
    description='My first ROS 2 package - learning ROS fundamentals',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'my_first_node = my_first_package.my_first_node:main',
        'my_first_subscriber = my_first_package.my_first_subscriber:main',
        'add_two_ints_server = my_first_package.add_two_ints_server:main',
        'add_two_ints_client = my_first_package.add_two_ints_client:main',
        'smart_light_node = my_first_package.smart_light_node:main',
    ],
},
)
