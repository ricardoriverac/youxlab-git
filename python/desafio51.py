soma = 0
for i in range(1, 7):
    numero = int(input(f'Digite o {i}º número: '))
    if numero % 2 == 0:
        soma += numero
print(f'\nA soma dos números pares é {soma}')
