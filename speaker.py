#speaker
import pygame

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

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
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load('reverse.mp3')
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()

def photo():
    pygame.mixer.music.load('photo.mp3')
    pygame.mixer.music.play()
    print('vudd')

def stop(): #Til þess að stoppa spilun
    pygame.mixer.music.stop()
