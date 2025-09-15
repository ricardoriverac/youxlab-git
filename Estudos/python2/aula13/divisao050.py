soma=0
for c in range(0, 7):
    valor1=int(input('Insira o valor: '))
    valor2=int(input('Insira o valor:'))
    valor3=int(input('Insira o valor: '))
    valor4=int(input('Insira o valor: '))
    valor5=int(input('Insira o valor: '))
    valor6=int(input('Insira o valor: '))
    divisao= c//2
    if c % divisao == 0:
        soma= soma+c
print(f'A soma dos números pares é {soma}')
