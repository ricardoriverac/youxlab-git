import random
import operator
jogadores=dict()
jogadoresOrdenados=[]
for c in range(1,6):
    sorteio= random.randint(0,6)
    jogadores[f'jogador{c}']= sorteio
for jogador, valor in jogadores.items():
    print(f'O {jogador} tirou o valor {valor} no dado')

jogadoresOrdenados = (sorted(jogadores.items(), key = operator.itemgetter(1), reverse=True))
print(jogadoresOrdenados)
for i, v in enumerate (jogadoresOrdenados):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')