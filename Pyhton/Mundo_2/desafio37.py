numero = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das bases para conversão:
[1] binário
[2] octal
[3] hexadecimal''')
binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)
opcoes = int(input('Escolha uma das opções: '))
if opcoes == 1:
    print(f'Sua conversão é binário {binario}')
elif opcoes == 2:
    print(f'Sua conervsão é octal {octal}')
elif opcoes == 3:
    print(f'Sua conversão é hexadecimal {hexadecimal}')