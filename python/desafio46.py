from random import randint
from time import sleep
print('=== JOKENPÔ ===')
print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
itens = ('PEDRA', 'PAPEL', 'TESOURA')
jogador = int(input('Qual é a sua jogada? '))
if jogador < 0 or jogador > 2:
    print('Jogada inválida! Você deve escolher 0, 1 ou 2.')
else:
    computador = randint(0, 2)
    print('JO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PÔ!!!')
    print('-=' * 15)
    print(f'Você jogou {itens[jogador]}')
    print(f'O computador jogou {itens[computador]}')
    print('-=' * 15)
    if jogador == computador:
        print('EMPATE!')
    elif (jogador == 0 and computador == 2) or \
         (jogador == 1 and computador == 0) or \
         (jogador == 2 and computador == 1):
        print('VOCÊ VENCEU! ')
    else:
        print('O COMPUTADOR VENCEU! ')
