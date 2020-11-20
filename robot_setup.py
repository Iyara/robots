# comments go here

import atexit
import time
from adafruit_crickit import crickit



class Robot:
    def __init__(self, left_trim=0, right_trim=0, stop_at_exit=True):

        self._left_trim = left_trim
        self._right_trim = right_trim
        if stop_at_exit:
            atexit.register(self.stop)

    def _left_speed(self, speed):
        # set the speed of the left motor, taking into account the trim offset
        assert -1 <= speed <= 1, "Speed must be a value between -1 to 1 inclusive!"
        speed += self._left_trim
        speed = max(-1, min(1, speed)) #constrain speed to 0-255 after trimming.
        crickit.continuous_servo_2.throttle = speed

    def _right_speed(self, speed):
        # set the speed of the right motor, taking into account the trim offset
        #print("speed ", speed)
        assert -1 <= speed <= 1, "Speed must be a value between -1 to 1 inclusive!"
        speed += self._right_trim
        speed = max(-1, min(1, speed)) #constrain speed to 0-255 after trimming.
        crickit.continuous_servo_1.throttle = speed


    @staticmethod
    def stop():
        # stop all movement
        crickit.continuous_servo_1.throttle = 0
        crickit.continuous_servo_2.throttle = 0

    def forward(self, speed, seconds=None):
        # move forward at the specified speed (0-255).
        # will start moving forward and then return unless a seconds value is specified,
        # in which case the robot will move forward for that amount of time and then stop.

        # set motor speed and move forward
        self._left_speed(speed)
        self._right_speed(speed)
        # if seconds are specified, move for that time and then stop
        if seconds is not None:
            time.sleep(seconds)
            self.stop()

    def steer(self, speed, direction):
        # move forward at the specified speed (0- 1). Direction is +- 1.
        # full left is -1, full right is +1
        if (speed + direction / 2) > 1:
            speed = (speed - direction / 2)  # calibrate so total motor output never goes above 1
        
        left = speed + direction / 2
        right = speed - direction / 2
        self._left_speed(left)
        self._right_speed(right)

    def right(self, speed, seconds=None):
        # spin to the right at the specified speed (0-255).
        # will start spinning and then return unless a seconds value is specified,
        # in which case the robot will spin for that amount of time and then stop.

        # set motor speed and move both forward
        self._left_speed(speed)
        self._right_speed(0)
        # if seconds are specified, move for that time and then stop
        if seconds is not None:
            time.sleep(seconds)
            self.stop()

    def left(self, speed, seconds=None):
        # spin to the left at the specified speed (0-255).
        # will start spinning and then return unless a seconds value is specified,
        # in which case the robot will spin for that amount of time and then stop.

        # set motor speed and move both forward
        self._left_speed(0)
        self._right_speed(speed)
        # if seconds are specified, move for that time and then stop
        if seconds is not None:
            time.sleep(seconds)
            self.stop()





        
