from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
print('VALORES SORTEADOS')
for k, v in jogo.items():
    print(f'O {k}, tirou {v} no dado.')
    sleep(0.5)
print(f'-='*4, 'CAMPEÕES', '=-'*4)
ranking = sorted(jogo.items(), reverse=True)
for k, v in enumerate(ranking):
    print(f'{k+1}º lugar: {v[0]} com {v[1]}.')