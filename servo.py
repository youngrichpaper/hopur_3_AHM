#servo
import time
from adafruit_servokit import ServoKit

# Initialize for 8 channels
kit = ServoKit(channels=8)


def testservo_1(): 
    kit.servo[0].angle = 180
    time.sleep(3)
    kit.servo[1].angle = 180
    time.sleep(5)
    kit.servo[1].angle = 0
    time.sleep(5)
    kit.servo[1].angle = 0

def rotate_s1(degree=90):
    kit.servo[0].angle = degree

def rotate_s2(degree=90):
    kit.servo[1].angle = degree




