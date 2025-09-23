import pygame
for t in range (0, 3):
    pygame.init()
    pygame.mixer.music.load('ex01.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()