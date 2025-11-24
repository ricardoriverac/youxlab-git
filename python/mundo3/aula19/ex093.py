# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade
# de gols feitos em cada partida.No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

jogador = {}
jogador["nome"] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
for p in range(partidas):
    q = int(input(f"Quantos gols na partida {p + 1}? "))
    gols.append(q)
    jogador["gols"] = gols
    jogador["total"] = sum(gols)
print(jogador)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")
for i, g in enumerate(jogador["gols"]):
 print(f'Na partida {i + 1}, fez {g} gols.')
print(f'Total de gols: {jogador["total"]}')