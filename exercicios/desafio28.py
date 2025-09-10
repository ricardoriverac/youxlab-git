from random import randint
computador = randint(0, 5)
print('vou pensar em um numero entre 0 e 5,vamos ver se você é capaz de adivinhar')
jogador = int(input('em qual numero eu pensei?'))
if jogador == computador:
    print('AEEEEEEEEEEEEEEEEEEE GANHOU SEU JÃO')
else:
    print('HAHAHAHAHA,humano insolente nao foi esse o numero,foi o {},não o {}'.format(computador, jogador))