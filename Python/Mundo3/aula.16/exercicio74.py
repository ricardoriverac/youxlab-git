import random
numeros_aleatorios = []
for v in range(5):
    numero = random.randint(1, 100)
    numeros_aleatorios.append(numero)
    tupla_numeros = tuple(numeros_aleatorios)
print(tupla_numeros)
minha_tupla = (numeros_aleatorios)
maior_valor = max(minha_tupla)
menor_valor = min(minha_tupla)
print(f'O maior valor é {maior_valor}, e o menor é {menor_valor}')