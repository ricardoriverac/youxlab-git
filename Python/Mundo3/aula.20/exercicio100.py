import random
numeros_disponivel = range(1,101)
numeros_sorteados = random.sample(numeros_disponivel, 5)
numeros_pares = 0
print(f'Os numeros sorteados foram {numeros_sorteados}')
for numero in numeros_sorteados:
    if numero % 2 == 0:
        numeros_pares += numero
print(f'Sendo os valores pares de {numeros_sorteados}, temos {numeros_pares}')