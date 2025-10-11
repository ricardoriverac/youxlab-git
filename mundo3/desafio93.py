jogador = []
partidas = []
nome = str(input('jogador: '))
tot = int(input('quantas partidas?: '))
for c in range(0,tot):
    partidas.append(int(input(f'quantos gols na partida {c}?')))
total = sum(partidas)
print (f'o total de gols em {tot} partidas foi de {total}, sendo:')
print(f'{partidas}')