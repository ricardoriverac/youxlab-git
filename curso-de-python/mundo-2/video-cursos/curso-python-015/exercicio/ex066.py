valor = soma = 0
count = 0
while valor != 999:
    valor = int(input('Digite um número (Digite 999 para parar): '))
    if valor == 999:
        break
    count += 1
    soma += valor
print(f'Você digitou {count} números, a soma de todos eles tem o resultado {soma}')