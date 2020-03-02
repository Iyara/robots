import time
from adafruit_crickit import crickit

print("1 Servo release demo!")

while True:
    print("Moving servo #1")
    crickit.servo_1.angle = 0      # right
    time.sleep(10)
    print("Released")
    crickit.servo_1._pwm_out.duty_cycle = 0
    time.sleep(10)
    # and repeat!

