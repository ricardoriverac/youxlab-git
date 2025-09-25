n = qntd = soma = 0
n = int(input('digite um número [999 para parar]: '))
while n != 999:
    soma += n
    qntd += 1
    n = int(input('digite um número [999 para parar]: '))
print(f'A quantidade de números foi de {qntd} e a soma entre eles foi de {soma}')