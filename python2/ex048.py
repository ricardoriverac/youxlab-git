soma = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
     soma = soma + c 
print(f'A soma dos numeros impares multiplos de tres entre 1 e 500 é {soma}')