soma=0
for c in range(1, 8):
    valor1=int(input('Insira o valor: '))  
    if valor1 % 2 == 0:
        soma = soma+valor1
print(f'A soma dos números pares é {soma}')
