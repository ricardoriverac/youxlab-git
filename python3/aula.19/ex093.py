"""Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, 
incluindo o total de gols feitos durante o campeonato."""



dicionario = {}
lista = []
dicionario['nome'] = str(input('Nome do jogador:'))
partidas = int(input('Quantas partidas ele jogou?'))
for c in range(1, partidas + 1):
    lista.append(int(input(f'Quantos gols ele fez na {c} partida ?')))
dicionario['gols'] = lista[:] 
dicionario['total'] = sum(dicionario['gols'])
print('-=' * 30)
for k, i in dicionario.items():
    print(f'O campo [{k}] tem valor {i}')
print('-=' * 30)
print(f'O jogador {dicionario["nome"]} jogou no total {partidas} partidadas')
for k, i  in enumerate(dicionario['gols']):
    print(f'na partida {k + 1}, ele fez {i} gols')
print(f'O total de gols foi {sum(dicionario["gols"])}')
