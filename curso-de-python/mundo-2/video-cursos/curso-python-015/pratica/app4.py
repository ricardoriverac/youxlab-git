numero = soma = 0
while numero != 999:
    numero = int(input('Digite um número: '))
    soma += numero
soma -= 999
print(f'A soma vale {soma}')