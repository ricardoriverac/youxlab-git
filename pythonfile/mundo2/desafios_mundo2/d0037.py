numero = int(input('Digite um numero inteiro'))
print('''escolha uma dads bases de conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção'))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)))
elif opção == 2:
    print ('{} convertido para OCTAL é {}'.format(numero, oct(numero))) 
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'. format(numero, hex(numero)))
else:
    print('Opção invalidade, tente novamente.')