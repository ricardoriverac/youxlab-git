numero = int(input('Digite um número: '))
print('Agora escolha um dos número a seguir: \n 1 BINÁRIO\n 2 OCTAL\n 3 HEXADECIMAL')
numero1 = int(input('Digite apenas um dos números acima: '))
if numero1 == 1:
    print(f'O número em binário é {bin(numero)[2:]}')
elif numero1 == 2:
    print(f'O número em octal é {oct(numero)[2:]}')
elif numero1 == 3:
    print(f'O número em hexadecimal é {hex(numero)[2:]}')
else:
    print('Por favor escolha uma das alternativas corretamente.')
