#servo

import ServoKit as s
import time

kit = s(channels=8)

def test_1():
    kit.servo[0].angle = 180
    time.sleep(3)
    kit.servo[1].angle = 180
    time.sleep(5)
    kit.servo[1].angle = 0
    time.sleep(5)
    kit.servo[1].angle = 0



        
