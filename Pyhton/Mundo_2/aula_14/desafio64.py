numero = total = conta = 0
while numero != 999:
    numero = int(input('Digite um número inteiro ou 999 para parar: '))
    if numero != 999:
        total = total + numero
        conta = conta + 1
print(f'{conta} números foram digitados/n a soma deles foi {total}')