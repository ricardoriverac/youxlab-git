soma = 0
for c in range(6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma = soma + numero
print(f'A resultado da soma dos números pares foi de: {soma}')
