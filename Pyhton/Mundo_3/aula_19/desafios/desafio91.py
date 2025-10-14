from random import randint
from time import sleep

jogos = {}         # Dicionário para guardar cada jogador e sua pontuação
ranking = []       # Lista que vai guardar os dados organizados para o ranking

print('Valores sorteados:')

# Sorteia os valores dos 4 jogadores
for i in range(1, 5):
    jogador = f'Jogador {i}'
    valor = randint(1, 6)  # Valor do dado (de 1 a 6)
    jogos[jogador] = valor
    print(f'{jogador} tirou {valor} no dado.')
    sleep(1)

# Cria o ranking com base nos valores 
ranking = sorted(jogos.items(), key=lambda x: x[1], reverse=True)

print('-' * 13)
print('== Ranking dos Jogadores ==')

# Mostra o ranking
for pos, (jogador, pontos) in enumerate(ranking):
    print(f'{pos+1}º lugar: {jogador} com {pontos}')