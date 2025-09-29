numero = int(input('Escolha um número: '))
print("""Escolha uma das bases para converter: 
      [1] converter para BINÁRIO
      [2] converter para OCTAL
      [3] converter para HEXADECIMAL""")
opcao = int(input('Escolha uma das bases: '))
binario = bin(numero)
octal = oct(numero)
hexadecimal =  hex(numero)
if opcao == 1:
    print(f'{numero} convertido para BINÁRIO é igual a {binario [2:]} ')
elif opcao == 2:
    print(f'{numero} convertido para OCTAL é igual a {octal [2:]}')
elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hexadecimal [2:]}')
