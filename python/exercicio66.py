soma = 0
cont = 0
num = int(input('digite um valor (999 para parar)'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('digite um valor (999 para parar)'))
print(f'foram digitados {cont} numeros e a soma de todos e {soma}')


