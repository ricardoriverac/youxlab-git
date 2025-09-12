from random import randint
computador=randint(0,5)#Faz o computador "PENSAR"
print('-=-'*10)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador=int(input('Em que numero eu pensei? '))#jogador tenta adivinhar
if jogador ==computador:
    print('Parabens voce conseguiu me vencer!')
else:
    print('Ops voce perdeu hahahaha!')