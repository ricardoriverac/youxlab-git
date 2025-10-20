# jogador = {}
# partidas = []
# jogador['nome'] = str(input('nome do jogador: '))
# total = int(input(f'quantas partidas {jogador['nome']} jogou? '))
# for c in range(0, total):
#     partidas.append(int(input(f'quantos gols na partida {c}?')))
# jogador['gols'] = partidas
# jogador['total'] = sum(partidas)
# print('-=' * 30)
# print(jogador)
# print('-=' * 30)
# for l, i in jogador.items():
#     print(f'o campo {l} tem o valor {i}')
# print(f'o jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.')
# for w, v in enumerate(jogador['nome']):
#     print(f' =>na partida {w}, fez {v} gols.')
# print(f'foi um total de {jogador['total']} gols.')



jogador = {}        # Dicionário 
partidas = []       # Lista 

# Entrada do nome do jogador
jogador['nome'] = str(input('Nome do jogador: '))

# Entrada da quantidade de partidas jogadas
total = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

# Entrada dos gols por partida
for c in range(total):
    gols = int(input(f"Quantos gols na partida {c}? "))
    partidas.append(gols)

# Armazenando os dados no dicionário
jogador['gols'] = partidas[:]              # Copia da lista de gols
jogador['total'] = sum(partidas)           # Soma total de gols

# Linha separadora
print('-=' * 30)

# Exibe o dicionário inteiro (estrutura bruta)
print(jogador)

# Linha separadora
print('-=' * 30)

# Exibe cada item do dicionário de forma detalhada
for chave, valor in jogador.items():
    print(f"O campo '{chave}' tem o valor {valor}")

# Exibe um resumo do desempenho
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")
for i, g in enumerate(jogador['gols']):
    print(f" Na partida {i}, fez {g} gols.")

# Exibe o total de gols
print(f"Foi um total de {jogador['total']} gols.")
