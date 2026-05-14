#servo
import time
from adafruit_servokit import ServoKit
import speaker

# Initialize for 8 channels
kit = ServoKit(channels=8)
flag_on = False

def rotate_s1(degree=90): #Snýr servo1 um ákveðna gráðu
    kit.servo[0].angle = degree

def rotate_s2(degree=90): #Snýr servo2 um ákveðna gráðu
    kit.servo[1].angle = degree

def wave_flag(controller): #Snýr servo fram og til (fyrir fána)
    while True:
        if controller.flag_on:
            if not speaker.music_channel.get_busy():
                speaker.mao()
            rotate_s2(180)
            time.sleep(0.7)
            rotate_s2(0)
            time.sleep(0.7)
        else:
            if speaker.music_channel.get_busy():
                speaker.stop()
            time.sleep(1)