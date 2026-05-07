#speaker
import pygame

pygame.mixer.init()

def ruski():
    pygame.mixer.load('ussr_anthem.mp3')
    pygame.mixer.play()

def baby():
    pygame.mixer.load('yhbaby.mp3')
    pygame.mixer.play()

def not_important():
    pygame.mixer.load('not-important.mp3')
    pygame.mixer.play()

def reverse():
    pygame.mixer.load('reverse.mp3')
    pygame.mixer.play()

def stop():
    pygame.mixer.stop()