soma = conta = 0 
while True:
    numero = int(input('Digite um valor (999 para quando quiser parar: '))
    if numero == 999: 
        break 
    conta += 1
    soma += numero
print(f'A soma dos {conta} valores foi {soma}!')