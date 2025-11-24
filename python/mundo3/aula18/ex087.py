#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = []
for l in range(3):
    linha_temp = []
    for coluna in range(3):
        num = int(input(f'Digite um número: '))
        linha_temp.append(num)
    matriz.append(linha_temp)
print('Matriz:')
for l in matriz:
    print(l)
soma_pares = 0
soma_tercei_colun = 0
segunda_linha = max(matriz[1])
for l in matriz:
    for valor in l:
        if valor % 2 == 0:
            soma_pares += valor
soma_tercei_colun = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'Soma dos valores pares: {soma_pares}')
print(f'Soma dos valores da terceira coluna: {soma_tercei_colun}')
print(f'Maior valor da segunda linha: {segunda_linha}')