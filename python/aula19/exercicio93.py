jogador = {}
lista = []
jogador['nome'] = str(input('Nome de jogador: '))
partidas = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? '))
for g in range(0, partidas):
    lista.append(int(input(f'Digite a quantidade de gols na partida {g}: ')))
    jogador['gols'] = lista[:]
    jogador['total'] = sum(lista)
print('-'*30)
print(jogador)
print('-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor: {v}')
print('-'*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador["gols"]):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]}')
print('-'*30)