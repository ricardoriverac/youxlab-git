# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

import random
from operator import itemgetter
from time import sleep
jogadores={
    'Jogador 1':random.randint(1, 6),
    'Jogador 2':random.randint(1, 6),
    'Jogador 3':random.randint(1, 6),
    'Jogador 4':random.randint(1, 6)
    }
print('Valores sorteados:')
for nome, valor in jogadores.items():
    print(f'  {nome} tirou {valor}')
    sleep(1)
rank=sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores:')
for i, v in enumerate(rank):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)

