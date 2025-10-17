#Escreva um programa em Python que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e
# 3 para hexadecimal.

number = int(input('Escolha um número inteiro: '))
print('Escolha a base de conversão: ')
print(' 1-Binário')
print('2-Octal')
print('3-Hexadecimal')
opcao = int(input('Opção: '))
if opcao == 1:
    binario = bin(number)
    print(f'O número {number} em binário é {binario}.')
elif opcao == 2:
    octal = oct(number)
    print(f'O número {number} em octal é {octal}.')
elif opcao == 3:
    hexadecimal = hex(number)
    print(f'O número {number} em hexadecimal é {hexadecimal}.')
else:
    print('Opção inválida!')