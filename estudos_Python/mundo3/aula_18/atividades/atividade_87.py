'''
Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

#Resposta

dados = []
soma_numeros_pares = []
maior_valor_segunda_coluna = []
contador = 0

for c in range(0, 9):
    contador += 1
    numero = int(input(f'Digite o {contador}° número: \n'))
    
    dados.append(numero)
    dados.sort()

    if numero % 2 != 0:
        soma_numeros_pares.append(numero)
    sum(soma_numeros_pares)


print(dados[0] , dados[1] , dados[2] )
print(dados[3] , dados[4] , dados[5] )
print(dados[6] , dados[7] , dados[8] )

soma_da_terceira_coluna = dados[2] + dados[5] + dados[8]
maior_valor_segunda_coluna.append(dados[1])
maior_valor_segunda_coluna.append(dados[4])
maior_valor_segunda_coluna.append(dados[7])

print(f'\nA soma de todos os valores pares: {sum(soma_numeros_pares)}')
print(f'A soma dos valores da terceira coluna: {soma_da_terceira_coluna}')
print(f'O maior valor da segunda linha: {max(maior_valor_segunda_coluna)}')


    