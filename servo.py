#servo

import ServoKit as p
import time

kit = p(channels=8)

def testservo_1():
    kit.servo[0].angle = 180
    time.sleep(3)
    kit.servo[1].angle = 180
    time.sleep(5)
    kit.servo[1].angle = 0
    time.sleep(5)
    kit.servo[1].angle = 0

def rotate_s1(degree):
    kit.servo[0].angle = 180



        
