# ROS 2 Six-Axis Robotic Arm

[![ROS 2](https://img.shields.io/badge/ROS%202-Humble-34a0a4)](https://docs.ros.org/en/humble/)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-e95420)](https://ubuntu.com/)
[![Python](https://img.shields.io/badge/Python-3.10-3776ab)](https://python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ed)](https://docker.com/)

A complete ROS 2 journey from beginner to advanced, culminating in a six-axis robotic arm simulation with MoveIt 2 motion planning.

---

## 📸 Project Showcase

| Joint State Publisher GUI | RViz with TF Frames |
|:-------------------------:|:-------------------:|
| ![Joint State GUI](docs/joint_state_gui.png) | ![RViz TF Frames](docs/rviz_frames.png) |

*Left: Joint state publisher controlling all 6 joints | Right: RViz displaying coordinate frames of each link*

---

## 🚀 Quick Start

### Prerequisites
- ROS 2 Humble Hawksbill
- Ubuntu 22.04 or Docker container
- MoveIt 2 installed

### Clone and Build
```bash
git clone https://github.com/Awande07/ros2-6axis-robot-arm.git
cd ros2-6axis-robot-arm
colcon build --packages-select ros2_advanced
source install/setup.bash
Launch the Six-Axis Arm

bash
ros2 launch ros2_advanced six_axis_moveit.launch.py

Run Joint State Publisher GUI
bash

ros2 run joint_state_publisher_gui joint_state_publisher_gui

Open RViz
bash

rviz2

In RViz:

    Add RobotModel (By display type)

    Set Fixed Frame to base_link

    Move sliders to see the arm move

Repository Structure
ros2_ws/
├── src/
│   ├── my_first_package/     # Chapters 1-3 (basic nodes)
│   ├── robot_monitor/        # Chapter 4 (parameters)
│   └── ros2_advanced/        # Chapters 5-18 (main project)
│       ├── urdf/             # Robot models (6-axis arm)
│       ├── launch/           # Launch files
│       ├── config/           # SRDF and controller configs
│       └── ros2_advanced/    # Python nodes
├── Dockerfile
└── README.md

Robot Specifications
Parameter	Value
Degrees of Freedom	6
Joint Types	Revolute (all)
Links	base_link, link1-6, tool_link
Joint Limits	±3.14 rad (varies by joint)
Geometry	Primitive shapes (boxes, cylinders)

Joint Configuration:
Joint	Axis	Range (rad)
joint1	Z	-3.14 to +3.14
joint2	Y	-2.00 to +2.00
joint3	Y	-2.50 to +2.50
joint4	Z	-3.14 to +3.14
joint5	Y	-1.50 to +1.50
joint6	Z	-3.14 to +3.14

Chapters Completed
Chapter	Topic	Status
0	Environment Setup (Docker + VS Code)	✅
1	First ROS 2 Package	✅
2	Topics & Subscribers	✅
3	Services	✅
4	Parameters	✅
5	Launch Files	✅
6	TF Transforms	✅
7	URDF Robot Modeling	✅
10	ROS 2 Actions	✅
11	MoveIt 2 Motion Planning	✅
18	Six-Axis Robotic Arm	✅

Key Commands
bash

# Build the workspace
colcon build --packages-select ros2_advanced

# Launch the complete system
ros2 launch ros2_advanced six_axis_moveit.launch.py

# Run pick and place sequence
ros2 run ros2_advanced pick_and_place

# Check transforms
ros2 run tf2_ros tf2_echo base_link link1

# List active nodes
ros2 node list

Verified Working Components

    robot_state_publisher loads all 7 links

    TF transforms publish correctly

    MoveIt planning pipeline loads OMPL

    joint_state_publisher_gui controls all 6 joints

    RViz displays TF frames and joint axes

    "You can start planning now!" confirmed

Known Limitations

Due to hardware limitations (Intel integrated graphics in Docker container), the 3D geometry (boxes, cylinders) does not render in RViz. However:

    ✅ TF frames are visible and move correctly

    ✅ All joints can be controlled

    ✅ MoveIt planning works

    ✅ The code is fully functional

The project can be visualized on any machine with proper GPU support by cloning this repository.

License

MIT License - see LICENSE file

Author

Awande Lindani Gcabashé

    GitHub: @Awande07

Acknowledgments

This project was completed as a second-year Applied Mathematics and Computer Science student, balancing coursework with limited hardware resources. Persistence > Perfect conditions.

