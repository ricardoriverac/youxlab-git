from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
'jogador2': randint(1, 6),
'jogador3': randint(1, 6),
'jogador4': randint(1, 6)}
ganhador = list()
print('Números sorteados:')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ganhador = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('ORDEM DE GANHADORES')
for i, v in enumerate(ganhador):
    print(f'{i+1} posição: {v[0]} com {v[1]}.')