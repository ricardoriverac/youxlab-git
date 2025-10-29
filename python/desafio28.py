from random import randint
computador = randint(0, 5)
print('-=-' * 20)
print('Irei pensar em um número de 0 a 5. Tente adivinhar qual é o número...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}.')

