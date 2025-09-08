import pygame
pygame.init()
pygame.mixer.music.load(input('Qual o arquivo para reproduzir?'))
pygame.mixer.music.play()
input()
pygame.event.wait()