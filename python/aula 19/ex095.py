jogador = dict()
partidas = list()
print('*'*50)
jogador['Nome'] = str(input('Digite o nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, total):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['Gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('*'*50)
print(jogador)
print('*'*50)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}. ')
print('*'*50)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for i, v in enumerate(jogador['Gols']):
    print(f'Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
print('*'*50)