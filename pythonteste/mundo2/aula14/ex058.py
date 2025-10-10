from random import randint
from time import sleep

tentativas = 0
computador = randint(0, 10)
print('Pensando em um número entre 0 e 10...')
sleep(1)
print('Pensei!')
sleep(1)
jogador = int(input('qual número eu pensei? '))
while jogador != computador:
    jogador = int(input('Errado, tente novamente '))
    tentativas += 1
print(f'Parabéns, eu pensei no número {computador} e você acertou após {tentativas} tentativas!')