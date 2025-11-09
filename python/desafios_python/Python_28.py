from random import randint
from time import sleep
computador = randint(0,5) #Faz o computador "PENSAR"
print('-=-=-' * 20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print('-=-=-' * 20)
jogador = int(input('Em que número eu pensei?')) # Jogador tenta adivinhar 
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Que pena tente outra vez')
