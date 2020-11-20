import time
from adafruit_crickit import crickit

print("multi Servo demo!")

# make a list of all the servos
#servos = (crickit.servo_1, crickit.servo_2, crickit.servo_3, crickit.servo_4)
servos = (crickit.servo_1, crickit.servo_2)

while True:
    # Repeat for all 4 servos
    for my_servo in servos:
        # Do the wave!
        print("Moving servo #", servos.index(my_servo)+1)
        my_servo.angle = 0      # right
        time.sleep(0.25)
        my_servo.angle = 90     # middle
        time.sleep(0.25)
        my_servo.angle = 180    # left
        time.sleep(0.25)
        my_servo.angle = 90     # middle
        time.sleep(0.25)
        my_servo.angle = 0      # right

