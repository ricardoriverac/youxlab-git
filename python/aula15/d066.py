numero = 0
soma = 0
quantidade = 0
numero = int(input('Digite um número: '))
while numero != 999:
    soma += numero
    quantidade += 1
    numero = int(input('Digite um número: '))
print(f'Foram digitados {quantidade} números, e a soma entre eles é igual a: {soma}')