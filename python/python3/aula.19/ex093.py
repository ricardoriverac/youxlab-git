jogador = dict()
lista = []
jogador['Nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador} jogou?: '))
for c in range(0, total):
   lista.append(int(input(f'Quantos gols ele fez na {c} partida?: ')))
jogador['gols'] = lista[:]
jogador['total'] = sum(lista)
print(jogador)
for j, v in jogador.items():
   print(f'O jogador {j} tem valor {v}')
print(lista)

