jogador = {}

jogador['nome'] = str(input('Digite o nome do Jogador: '))
jogador['partidas'] = int(input('Quantas partidas ele jogou? '))

gol = []

for g in range(1, jogador['partidas'] + 1):
    gol.append(int(input(f'Quantos gols ele fez na {g}ª partida? ')))

jogador['gols'] = gol
jogador['totalGols'] = sum(gol)

print('-' * 20)
print(f'O jogador \033[33m{jogador["nome"]}\033[m jogou \033[33m{jogador["partidas"]}\033[m partidas')

for i, v in enumerate(jogador['gols']):
    print(f'-- Na partida \033[33m{i}\033[m, fez \033[33m{v}\033[m gols.')

print(f'\033[33m{jogador["nome"]}\033[m fez no total \033[33m{jogador["totalGols"]}\033[m gols.')