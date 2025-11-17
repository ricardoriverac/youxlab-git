import pygame # type: ignore
pygame.init()
pygame.mixer.music.load('ex021a.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()