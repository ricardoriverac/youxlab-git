soma = 0
for c in range(6):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0 :
        soma = soma + numero
print(f'A soma dos pares é {soma}')
