'''
Faça um programa am Python que abra a reproduza o áudio de um arquivo MP3.
'''

#Resposta

import pygame
pygame.init()
pygame.mixer.music.load('estudos_python/aula_008/atividades/dirigir.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
