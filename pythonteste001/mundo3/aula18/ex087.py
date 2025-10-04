matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = somaColuna3 = maiorLinha2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^3}]', end= '')
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
    print()
print(f'A soma dos valores pares é {somaPar}')
for l in range(0, 3):
    somaColuna3 += matriz[l][2]
print(f'A soma dos números da coluna 3 é {somaColuna3}')
for c in range(0, 3):
    if c == 0:
        maiorLinha2 = matriz[1][c]
    else:
        maiorLinha2 = matriz[1][c]
print(f'O maior número da 2ª linha é {maiorLinha2}')