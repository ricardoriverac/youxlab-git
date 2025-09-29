import random
for c in range(1, 11):
    numeroAleatorio = random.randint(1,10)
    valorUsuario = int(input('Adivinhe o numero que estou pensando de 1 a 10: '))
    palpite = 0
    while numeroAleatorio == valorUsuario:
        if valorUsuario != numeroAleatorio:
            print('x-X , Você errou! Tente novamente!')
            palpite += 1
        elif valorUsuario == numeroAleatorio:
            print('PARABÉNS!! Você acertou o número que eu estava pensando!')
print(f'Foram necessário {palpite} palpites até você acerta o número correto.')
'''import random 
valorUsuario = int(input('Adivinhe o número que estou "pensando" de 1 a 10: '))
numeroAleatorio = random.randint(1,10)
print('E o número era...')
print(f'O número {numeroAleatorio}!')
if valorUsuario == numeroAleatorio:
    print('PARABÉNS! Você acertou o número que eu estava pensando!')
else:
    print('x-X , Você errou! Tente novamente!')'''