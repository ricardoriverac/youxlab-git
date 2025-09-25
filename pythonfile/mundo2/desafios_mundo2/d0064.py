contador = 0
numero=0
soma = 0
while  numero != 999:
        numero = int(input('Digite outro numero (999 para encerrar)'))
        contador +=1
        soma += numero
print(f'{contador}')
print(f'A soma de todos eles foi {soma-999}')