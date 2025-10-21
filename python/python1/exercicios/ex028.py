from random import randint
from time import sleep
comp = randint(0,5)
print('Vou pensar em um número tente adivinhar: ')
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == comp:
    print('Você acertou! PARABENS!')
else:
    print('Você errou! TENTE NOVAMENTE')    
    