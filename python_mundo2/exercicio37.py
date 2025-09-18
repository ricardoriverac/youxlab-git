numero = int(input(' digite um numero inteiro:'))
print('digite 1  binario para digite 2 octal para ou digite 3 para hexadecimal ')
conta = int(input('digite o escolhido: '))
if conta == 1:
    print('{} convertido para BINARIO é igual a {}'.format(numero, bin(numero)[2:]))
elif conta == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct (numero)[2:]))
elif conta == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('opçao invalida. tente novamente')  