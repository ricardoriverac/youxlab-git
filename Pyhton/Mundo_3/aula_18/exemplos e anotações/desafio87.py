matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
soma =  0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        numero = (int(input(f'Digite o número [{c, l}]: ')))
        matriz[l][c] = numero
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5}', end='')
        if matriz[l][c] % 2 == 0:
            pares = pares + matriz[l][c]
    soma = soma + matriz[l][2]
    print()
maior = max(matriz[1][0], matriz[1][1], matriz[1][2])
print('=' * 30)
print(f'Soma dos valores pares: {pares}')
print(f'Soma dos valores da 3ª coluna: {soma}')
print(f'Maior valor da 2ª coluna: {maior}')