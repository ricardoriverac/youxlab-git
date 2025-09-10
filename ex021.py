import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Caminho para o arquivo MP3
mp3_path = "/home/youx/Downloads/core-rage-mais-estourado.mp3"

# Carrega e toca o arquivo MP3
pygame.mixer.music.load(mp3_path)
pygame.mixer.music.play()

# Aguarda até a música terminar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)