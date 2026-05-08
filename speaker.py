# #speaker
# import pygame

# pygame.init()
# pygame.mixer.init()

# def ruski():
#     pygame.mixer.music.unload()
#     pygame.mixer.music.load('ussr_anthem.mp3')
#     pygame.mixer.music.play()

# def baby():
#     pygame.mixer.music.unload()
#     pygame.mixer.music.load('yhbaby.mp3')
#     pygame.mixer.music.play()

# def not_important():
#     pygame.mixer.music.unload()
#     pygame.mixer.music.load('not-important.mp3')
#     pygame.mixer.music.play()

# def reverse():
#     # pygame.mixer.music.unload()
#     pygame.mixer.music.load('reverse.mp3')
#     pygame.mixer.music.set_volume(1.0)
#     pygame.mixer.music.play()

# def stop():
#     pygame.mixer.music.unload()
#     pygame.mixer.music.stop()

#speaker
import pygame

pygame.init()
pygame.mixer.init()

MAX_VOLUME = 1.0
pygame.mixer.music.set_volume(MAX_VOLUME)


def play_music(filename):
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(MAX_VOLUME)
    pygame.mixer.music.play()


def ruski():
    play_music('ussr_anthem.mp3')


def baby():
    play_music('yhbaby.mp3')


def not_important():
    play_music('not-important.mp3')


def reverse():
    play_music('reverse.mp3')


def stop():
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()