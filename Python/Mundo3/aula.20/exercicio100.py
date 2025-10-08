import random

def sorteia(numeros_disponivel):
    return  random.sample(numeros_disponivel, 5)

def somaPar(numeros_sorteados):
    soma = 0

    for numero in numeros_sorteados:
        if numero % 2 == 0:
            soma += numero
    return soma

numeros_disponivel = range(1,101)
numeros_sorteados = sorteia(numeros_disponivel)
print(f'Os numeros sorteados foram {numeros_sorteados}')
numeros_pares = somaPar(numeros_sorteados)
print(f'Sendo os valores pares de {numeros_sorteados}, temos {numeros_pares}')