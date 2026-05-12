# speaker.py
import pygame

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

# Býr til mismunandi channels
music_channel = pygame.mixer.Channel(0)
effect_channel = pygame.mixer.Channel(1)
voice_channel = pygame.mixer.Channel(2)

# Hleður inn hljóðum sem Sound objects
baby_sound = pygame.mixer.Sound('yhbaby.mp3')
not_important_sound = pygame.mixer.Sound('not-important.mp3')
reverse_sound = pygame.mixer.Sound('reverse.mp3')
photo_sound = pygame.mixer.Sound('photo.mp3')
mao_sound = pygame.mixer.Sound('mao.mp3')


def baby():
    effect_channel.play(baby_sound)


def not_important():
    effect_channel.play(not_important_sound)


def reverse():
    if not voice_channel.get_busy():
        voice_channel.set_volume(1.0)
        voice_channel.play(reverse_sound)


def photo():
    voice_channel.play(photo_sound)
    print('vudd')


def mao():
    music_channel.play(mao_sound)


def stop():
    music_channel.stop()
    effect_channel.stop()
    voice_channel.stop()