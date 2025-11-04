matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_coluna3 = maior_linha2 = 0
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=' * 30)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-=' * 30)
for linha in range(3):
    for coluna in range(3):
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
for linha in range(3):
    soma_coluna3 += matriz[linha][2]
maior_linha2 = max(matriz[1])
print(f'A) A soma dos valores pares é {soma_pares}')
print(f'B) A soma dos valores da terceira coluna é {soma_coluna3}')
print(f'C) O maior valor da segunda linha é {maior_linha2}')
