numero = contador = 0
while contador < 5:
    numero = int(input('Digite um número: '))
    contador += 1
print('='*40)

numero1 = soma = 0
while numero1 != 999:
    numero1 = int(input('DIgite um valor: '))
    soma += numero1
soma -= 999
print(f'A soma entre os números vale {soma} ')
print('='*40)

numero = soma = 0
while True:
    numero = int(input('Escreva um número qualquer: '))
    if numero == 999:
        break
    soma1 += numero
print(f'A soma dos números vale {soma}')