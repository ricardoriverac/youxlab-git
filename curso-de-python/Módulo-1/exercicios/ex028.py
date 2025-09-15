import random 
valorUsuario = int(input('Adivinhe o número que estou "pensando" de 1 a 5: '))
numeroAleatorio = random.randint(1,5)
print('E o número era...')
print(f'O número {numeroAleatorio}!')
if valorUsuario == numeroAleatorio:
    print('PARABÉNS! Você acertou o número que eu estava pensando!')
else:
    print('x-X , Você errou! Tente novamente!')