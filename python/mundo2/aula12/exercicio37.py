numero=int(input('Digite um numero inteiro: '))
print('''Escola uma das bases para convenrsão: 
[1] converte para BINARIO
[2] converte para OCTAL
[2] converte para HEXADECIMAL''')
opção=int(input('Sua opção: '))
if opção ==1:
    print(f'{numero}convertido para BINARIO é igual a {numero, bin(numero)}')
elif opção == 2:
    print(f'{numero} convertido para OCTAL é igual a {numero, oct(numero)}')
elif opção == 3:
     print(f'{numero} convertido para HEXADECIMAL é igual a {numero, hex(numero)}')   
else:
    print('Opção invalida. Tente novamente.')     