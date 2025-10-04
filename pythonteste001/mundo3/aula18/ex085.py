numero = [[], []]
numeros = 0
for c in range(1, 8):
    numeros = int(input(f'Digite o {c}º numero: '))
    if numeros % 2 == 0:
        numero[0].append(numeros)
    else:
        numero[1].append(numeros)
numero[0].sort()
numero[1].sort()
print(f'Os numero pares são {numero[0]}')
print(f'Os numeros impares são {numero[1]}')
