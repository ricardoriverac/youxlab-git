jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, total):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print(jogador)
for k, v in jogador.items():
    print(f'{k}: {v}')
    print(f'{jogador["Nome"]} jogou {len(jogador["Gols"])} partidas')
for i, v in enumerate (jogador['Gols']):
    print(f'Na partida {i}, fez {v} gols')
    print(f'Foi um total de {jogador["Total"]} gols')