import pygame

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (M) '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif 40 <= imc < 65:
    print('Você está em OBESIDADE MÓRBIDA!')
else:  # IMC 65 ou mais
    pygame.mixer.init()
    mp3_path = "/home/youx/Downloads/cat-laughing.mp3"
    pygame.mixer.music.load(mp3_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

print('O IMC desta pessoa é {:.1f}'.format(imc))