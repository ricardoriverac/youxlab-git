# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#  No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print('Digite os valores para a matriz 3x3: ')
for linha in range(0, 3):
    for coluna in range(0, 3):
            matriz[linha][coluna] = int(input(f'valor da posição [{linha}] [{coluna}]: '))

print('\nMatriz formatada: ')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()





