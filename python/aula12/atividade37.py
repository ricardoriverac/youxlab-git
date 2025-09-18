numInt = int(input('Digite um número inteiro: '))
escolha = int(input('''Digite um número sendo: 
    [ 1 ] para binário; 
    [ 2 ] para octal; 
    [ 3 ] para hexadecimal.
    Qual sua escolha? R:  '''))
if escolha == 1:
    print(f'O número inteiro {numInt}, em binário, é igual a {bin(numInt)[2:]}')
elif escolha == 2:
    print(f'O número inteiro {numInt}, em octal, é igual a {oct(numInt)[2:]}')
elif escolha == 3:
    print(f'O número inteiro {numInt}, em hexadecimal, é igual a {hex(numInt)[2:]}')
else:
    print('Opção inválida. \nTente novamente.')
    #ao converter um dígito, encontra-se no resultado o prefixo "0b" ou "0o" ou "0x", dependendo do sistema numérico no qual o usuário preferiu inverter. 
    #Nada mais é que o sistema identificando aquele valor como pertencente a um sistema numérico. 
    #O "0" significa que o número é uma constante e o resto significa o sistema numérico pertencente
    #Para resolver isso, podemos apenas usar o fatiamento dos dois primeiros dígitos do resultado
    #usando [2:]