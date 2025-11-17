from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
        }

rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for k, v in jogo.items():
    print(f'{k} caiu com o número {v}')
    sleep(1)

print('-' * 25)
print(f'{"--RANK DE VITÓRIA--":^25}')
print('-' * 25)

for p, v in enumerate(rank):
    print(f'{p + 1}º lugar: {v[0]} com o número {v[1]} ')
    sleep(1)