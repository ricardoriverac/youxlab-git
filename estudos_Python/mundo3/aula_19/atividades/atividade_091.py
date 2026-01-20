'''
 Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses 
 resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que 
 o vencedor tirou o maior número no dado.
'''

#Resposta
import random

dados = {}


for c in range(0, 4):
    n_aleatorio = random.randint(1, 6)
    dados[f'jogador {c+1}'] = n_aleatorio
for c, v in enumerate(dados.values()):
    print(f'O {c+1}° jogador tirou: {v}')
sorted(dados.values(), reverse=True)
print()
print('Posições dos ganhadores:')
for b, v in enumerate(sorted(dados.values(), reverse=True)):
    print(f'O {b+1}° lugar ficou o: {v}')
    