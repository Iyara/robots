import time
from adafruit_crickit import crickit

print("1 Continuous Servo demo!")

while True:
    crickit.continuous_servo_1.throttle = 1.0 # Forwards
    time.sleep(2)
    crickit.continuous_servo_1.throttle = 0.5 # Forwards halfspeed
    time.sleep(2)
    crickit.continuous_servo_1.throttle = 0   # Stop
    time.sleep(2)
    crickit.continuous_servo_1.throttle = -0.5 # Backwards halfspeed
    time.sleep(2)
    crickit.continuous_servo_1.throttle = -1 # Forwards
    time.sleep(2)
    crickit.continuous_servo_1.throttle = 0   # Stop
    time.sleep(2)

