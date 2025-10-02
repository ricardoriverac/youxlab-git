from random import randint
computador = randint(0, 10)
print('Eu sou o computador... Acabei de pensar em um numero entre 0 e 10')
print('Será se voce consegue advinhar qual que foi?')
acertou = False
while not acertou:
    jogador = int(input('Qual o seu palpite?'))
    if jogador == computador:
        acertou = True
        print('Acertou!')
        print('Parabens,voce acertou!')