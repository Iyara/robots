# comments

import time
import robot_setup

LEFT_TRIM = 0
RIGHT_TRIM = 0

# create an instance of the robot with the specified trim values
robot = robot_setup.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

# now move the robot around!
# Each call below takes two parameters:
#  - speed: The speed of the movement, a value from -1.0 to +1.0.  The higher the value
#           the faster the movement.  You need to start with a value around 0.10
#           to get enough torque to move the robot.
#  - time (seconds):  Amount of time to perform the movement.  After moving for
#                     this amount of seconds the robot will stop.  This parameter
#                     is optional and if not specified the robot will start moving
#                     forever.

print("forward 10")
robot.forward(0.5, 10)

"""
print("steer")
robot.steer(0.5, 0)

print("Left")
robot.left(0.5, 3)
print("Right")
robot.right(0.5, 3)
print("Steer")
# second argument is direction--full left is -1, full right is +1
robot.steer(0.5, 0.5)
print("Sleep")
time.sleep(3)
"""

print("stop")
robot.stop()

print("Done.")

