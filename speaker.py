#speaker
import os
from subprocess import call

def ruski():
    os.system('mpg123 ussr_anthem.mp3')

def baby():
    os.system('mpg123 yhbaby.mp3')

def not_important():
    os.system('mpg123 not-important.mp3')

def reverse():
    bakk = call(["aplay", "/home/reverse.mp3"])
