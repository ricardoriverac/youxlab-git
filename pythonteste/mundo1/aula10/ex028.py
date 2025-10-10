from random import randint
from time import sleep

computador=randint(0,5) #faz o computador pensar
print('-=-'*20)
print('vou pensar em um número entre 0 e 5. tente adivinhar...')
print('-=-'*20)
jogador=int(input('em que múmero eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABENS! você conseguiu me vencer!')
else:
    print('GANHEI! eu pensei no número {} e não no {}!'.format(computador,jogador))