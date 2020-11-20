# test why continuous servos aren't cooperating

import time
from adafruit_crickit import crickit

print("cont servo 2 test")

while True:
    crickit.continuous_servo_2.throttle = 1.0 # forward

