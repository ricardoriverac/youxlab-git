pares = list()
impares = list()
numero = list()
while True:
    numero.append(int(input('Digite um número:')))
    continuar = str(input('Quer continuar? [S/N]:'))
    if continuar in 'Nn':
        break
for i, v in enumerate(numero):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {numero}')
print(f'A lista de pares é {pares}')
print(f'A lista ímpares é {impares}')

