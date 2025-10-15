matriz = []

soma = 0
somaLinhaTres = 0

for linhas in range(0, 3):
    linha = []
    for coluna in range(0, 3):
        coluna = int(input(f'Digite um número para a posição [{linhas}, {coluna}]: '))
        linha.append(coluna)

        if coluna % 2 == 0:
            soma += coluna

    matriz.append(linha[:])
    linha.clear()

for linhas in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linhas][coluna]:^5}]', end='')
    print()
print()

print(f'A soma de todos os números pares da matriz tem o resultado: \033[33m{soma}\033[m')
print(f'A soma de todos os números da terceira linha tem o resultado: \033[33m{matriz[0][2] + matriz[1][2] + matriz[2][2]}\033[m')
print(f'O maior número da segunda linha é o número: \033[33m{max(matriz[1])}\033[m')