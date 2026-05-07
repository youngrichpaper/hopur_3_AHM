#speaker
import os
from subprocess import Popen

def ruski():
    os.system('mpg123 ussr_anthem.mp3')

def baby():
    os.system('mpg123 yhbaby.mp3')

def not_important():
    os.system('mpg123 not-important.mp3')

def reverse():
    global bakk
    bakk = Popen(["mpg123", "/home/hopur_3/reverse.mp3"])
    return bakk

def reverse_stop():
    global bakk

    if bakk:
        bakk.terminate()