#!/usr/bin/env python3
"""Simple script to verify MoveIt Python API is accessible."""

import sys

try:
    print("Checking MoveIt imports...")
    
    # These are the core MoveIt Python modules
    from moveit_commander import MoveGroupCommander, RobotCommander, PlanningSceneInterface
    print("✅ moveit_commander imported successfully")
    
    from moveit_msgs.msg import RobotState, MotionPlanRequest
    print("✅ moveit_msgs imported successfully")
    
    print("\n🎉 MoveIt Python API is ready to use!")
    print("Your six-axis arm can use MoveIt for motion planning.")
    
except ImportError as e:
    print(f"❌ Import failed: {e}")
    print("\nMoveIt Python API may not be available.")
    print("This is expected in some Humble installations.")
    sys.exit(1)

if __name__ == "__main__":
    pass