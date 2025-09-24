soma = 0
cont = 0
for d in range(1, 7):
    num = int(input(f'Digite o {d} valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} números PARES e a soma foi {soma}')