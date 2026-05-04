#servo
import time
from adafruit_servokit import ServoKit

# Initialize for 8 channels
kit = ServoKit(channels=8)


def rotate_s1(degree=90):
    kit.servo[0].angle = degree

def rotate_s2(degree=90):
    kit.servo[1].angle = degree

# rotate_s1(90) #setja í 0 til að horfa til hliðar
# time.sleep(4)
# rotate_s2(90) #setja í 180 til að horfa til hliðar

try:
    while True:
        rotate_s1(20) 
        rotate_s2(160)
        time.sleep(0.5)
        rotate_s1(90) 
        rotate_s2(90)

except KeyboardInterrupt:
    pass

