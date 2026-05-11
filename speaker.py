#speaker
import pygame

pygame.init()
pygame.mixer.init()

def ruski():
    pygame.mixer.music.load('ussr_anthem.mp3')
    pygame.mixer.music.play()

def baby():
    pygame.mixer.music.load('yhbaby.mp3')
    pygame.mixer.music.play()

def not_important():
    pygame.mixer.music.load('not-important.mp3')
    pygame.mixer.music.play()

def reverse():
    pygame.mixer.music.load('reverse.mp3')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()

def stop(): #Til þess að stoppa spilun
    pygame.mixer.music.stop()
