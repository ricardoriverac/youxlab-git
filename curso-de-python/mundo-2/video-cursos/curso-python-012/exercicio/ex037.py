numero = int(input('Digite um número: '))
escolha = int(input('Digite uma opção de 1 a 3: '))

if escolha == 1:
    print(f'O número {numero} convertido para binário fica {bin(numero)}')

if escolha == 2:
    print(f'O número {numero} convertido para octal fica {oct(numero)}')

if escolha == 3:
    print(f'O número {numero} convertido para hexadecimal fica {hex(numero)}')