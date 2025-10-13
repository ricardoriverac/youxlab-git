# # Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
# # A) A soma de todos os valores pares digitados.
# # B) A soma dos valores da terceira coluna.
# # C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = 0
somaTerceiraColuna = 0
maiorSegundaLinha = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha][coluna] = valor

        if valor % 2 == 0:
            somaPares += valor

        if coluna == 2:
            somaTerceiraColuna += valor
        
        if linha == 1:
            if valor > maiorSegundaLinha:
                maiorSegundaLinha = valor

print('-=' * 15)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

print('-=' * 15)
print(f'A soma dos valores pares é: {somaPares}')
print(f'A soma dos valores da terceira coluna é: {somaTerceiraColuna}')
print(f'O maior valor da segunda linha é: {maiorSegundaLinha}')

      