numeroInteiro = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:'
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
resposta = int(input('Sua opcção:'))
if resposta == 1:
    print('{} A conversão binária será a seguinte {}'.format(numeroInteiro, bin(resposta)))

elif resposta == 2:
    print('{} A conversão octal será a segui1nte {}'.format(numeroInteiro, oct(numeroInteiro)))

elif resposta == 3:
    print('{} A conversão para hexadecimal {}'.format(numeroInteiro, hex(numeroInteiro)))
