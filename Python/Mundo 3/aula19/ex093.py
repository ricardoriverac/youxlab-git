# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
golsPartida = []
totalGols = 0

jogador['nome'] = input('Nome do jogador: ')

partidas = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? '))
for i in range(partidas):
    gols = int(input(f'Quantos gols na partida {i+1}? '))
    golsPartida.append(gols)
    totalGols += gols

jogador['gols'] = golsPartida
jogador['totalGols'] = totalGols
print('-=-='*30)
print(f'DADOS DO JOGADOR')
print(f'Nome: {jogador["nome"]}')
print(f'Gols por partida: {jogador["gols"]}')
print(f'Total de gols: {jogador["totalGols"]}')
print(f'Aproveitamento: O jogador marcou {jogador["totalGols"]} gols em {partidas} jogos.')

















