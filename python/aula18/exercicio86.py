matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = maior = soter = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
    print()
print(soma)
for l in range(0, 3):
    soter += matriz[l][2]
print(soter)