soma = 0
cont = 0
for impares in range(1, 501, 2):
    if impares % 3 == 0: 
        cont += 1
        soma += impares
print(f'A soma de {cont} números é {soma}', end= ' ')