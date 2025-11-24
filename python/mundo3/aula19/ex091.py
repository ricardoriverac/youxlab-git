#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
# resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo
# que o vencedor tirou o maior número no dado.

import random
jogadores = {"j1","j2","j3","j4"}
resultados = {}
for j in jogadores:
    resultados[j] = random.randint(1,6)
print('Resultados:')
for nome, valor in resultados.items():
    print(f'{nome}: {valor}')
maior = max(resultados.values())
vencedores = [nome for nome, valor in resultados.items() if valor == maior]
if len(vencedores) == 1:
    print(f'Vencedor: {vencedores[0]} com {maior} pontos.')
else:
    print(f"Empate entre {','.join(vencedores)} todos com {maior} ponto.")