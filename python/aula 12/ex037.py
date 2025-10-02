numero_inteiro = int(input('Digite um número inteiro: '))
base_conversao = int(input('Qual será a forma de conversão?\n1- binário\n2- octal\n3- hexadecimal\n'))
if base_conversao == 1: 
    print('O {} convertido para binário é igual a {}'.format(numero_inteiro, bin(numero_inteiro)))
elif base_conversao == 2: 
    print('O {} convertido para octal é igual a {}'.format(numero_inteiro, oct(numero_inteiro)))
elif base_conversao == 3: 
    print('O {} convertido para hexadecimal é igual a {}'.format(numero_inteiro, hex(numero_inteiro)))
else:
    print('Opção inválida')