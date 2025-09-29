from time import sleep
import pygame
for contagem in range(10, -1, -1):
    print(contagem)
    sleep(1)
pygame.mixer.init()
mp3_path = "/home/youx/Downloads/som_de_queima_de_fogos_mp3_www.mp3"
pygame.mixer.music.load(mp3_path)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
    