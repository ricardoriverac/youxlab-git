soma = 0
contador = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    soma += num
    contador += 1
print(f'Você digitou {contador} números.')
print(f'A soma dos valores digitados é {soma}.')
