n = 0
soma= 0
while True:
    n= float(input('Escolha um valor: '))
    if n == 999:
        break
    soma=soma+n
print(f'A soma vale {soma}')
