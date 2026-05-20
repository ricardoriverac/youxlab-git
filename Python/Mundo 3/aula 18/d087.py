matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = maior = somaColuna = 0
print('-'*25)
print('    INICIANDO PROGRAMA   ')
print('-'*25)
for l in range(0, 3):
    for f in range(0, 3):
        matriz[l][f] = int(input(f'->''Número para a sua matriz [{l}, {f}]: '))
print('-'*50)
for l in range(0, 3):
    for f in range(0, 3):
        print(f'[{matriz[l][f]:^5}]', end='')
        if matriz[l][f] % 2 == 0:
            somaPar += matriz[l][f]
    print()
print('-'*50)
print(' SOMA DOS NÚMEROS PARES: ')
print(f'-A soma dos números pares da matriz é: {somaPar}.')
for l in range(0, 3):
    somaColuna += matriz[l][2]
print('-'*50)
print(' SOMA DA TERCEIRA COLUNA DA MATRIZ: ')
print(f'-A soma da terceira coluna da matriz é: {somaColuna}.')
for f in range(0, 3):
    if f == 0:
        maior = matriz[1][f]
    elif matriz[1][f] > maior:
        maior = matriz[1][f]
print('-'*50)
print(' MAIOR NÚMERO DA SEGUNDA LINHA: ')
print(f'-O maior número da segunda linha é: {maior}.')
