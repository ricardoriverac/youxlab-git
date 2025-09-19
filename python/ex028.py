from random import randint
computador = randint(0, 5) # Faz o computador "PENSAR"
print('me deixe pensar em um número entre 0 e 5. Tente adivinhar...')
print()
pessoa = int(input('Em que número eu pensei? ')) # A pessoa tenta advinhar
if pessoa == computador:
    print('PARABÉS, você conseguiu me ganhar!')
else: 
    print('GANHEEEI, eu pensei no número {} e não no {}!'.format(computador, pessoa))



