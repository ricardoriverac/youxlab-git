from random import randint
from time import sleep
from operator import itemgetter
dic = {}
jogadores = {}
dic= {'Jogador1': randint(1, 6),
    'Jogador2': randint(1,6),
    'Jogador3': randint(1,6),
    'Jogador4': randint(1,6)}
for v, k in dic.items():
    print(f'O {v} jogou {k} no dado!')
    sleep(1)
jogadores = sorted(dic.items(), key=itemgetter(1), reverse=True)
for i, k in enumerate(jogadores):
    print(f'posição {i+1}: {k[0]} e tirou no {k[1]} dado')
    sleep(1)
