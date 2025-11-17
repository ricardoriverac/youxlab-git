matriz = []

for linhas in range(0, 3):
    linha = []
    for coluna in range(0, 3):
        coluna = int(input(f'Digite um número para a posição [{linhas}, {coluna}]: '))
        linha.append(coluna)

    matriz.append(linha[:])
    linha.clear()

for linhas in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linhas][coluna]:^5}]', end='')
    print()