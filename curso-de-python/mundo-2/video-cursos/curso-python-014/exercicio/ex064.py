valor = soma = 0
count = 0

while valor != 999:
    valor = int(input('Digite um número (Digite 999 para parar): '))
    count += 1
    soma += valor
soma -= 999

print(f'Você digitou {count} números, a soma de todos eles tem o resultado {soma}')