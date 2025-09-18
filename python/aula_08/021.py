import pygame
pygame.mixer.init()
pygame.mixer.music.load('sample-6s.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()