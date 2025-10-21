numero = int(input('Digite um numero inteiro: '))
print("""Digite a base de convercao: 
      [1] Para binario
      [2] Para octal
      [3] Para hexadecimal""")
binario = bin(numero)
octal = oct(numero)
hexadecimal= hex(numero)
opcao = int(input(f'Escolha uma das opcoes: '))
if opcao  == 1:
    print(f'Sua conversao sera binario {binario}')
elif opcao == 2:
    print(f'Sua conversao sera octal {octal}')
elif opcao == 3:
    print('Sua conversao vai ser hexadecimal{hexadecimal}')

