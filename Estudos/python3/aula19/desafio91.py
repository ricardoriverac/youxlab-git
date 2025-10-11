import random
jogadores=dict()
for c in range(0,5):
    sorteio= random.randint(0,6)
    jogadores[f'jogador{c}']= sorteio
for jogador, valor in jogadores.items():
    print(f'O {jogador} tirou o valor {valor} no dado')
sorted(jogadores, reverse=True)