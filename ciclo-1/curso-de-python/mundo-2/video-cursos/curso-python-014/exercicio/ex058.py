import random
numeroAleatorio = random.randint(1,10)
valorUsuario = 0
palpite = 0

while numeroAleatorio != valorUsuario:
        numeroAleatorio = random.randint(1,10)
        valorUsuario = int(input('Adivinhe o numero que estou pensando de 1 a 10: '))

        if valorUsuario != numeroAleatorio:
            print('x-X , Você errou! Tente novamente!')
            palpite += 1
        else:
            print('PARABÉNS!! Você acertou o número que eu estava pensando!')

print(f'Foram necessário {palpite} palpites até você acerta o número correto.')