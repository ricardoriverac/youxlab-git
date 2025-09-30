# CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔNICO. NO INÍCIO, PERGUNTE AO USÚARIO QUAL SERÁ O VALOR A SER SACADO (NÚMERO INTEIRO) 
# E O PROGRAMA VAI INFORMAR QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES
print('CAIXA ELETRÔNICO')
quantidadeDinheiro = 0
resto = 0
valorSaque = int(input('Digite qual será o valor sacado: R$ '))
if valorSaque < 100:
    print(f'A quantidade de notas de R$100 reais é 0')
else:
    quantidadeDinheiro = valorSaque // 100
    print(f'A quantidade de notas de R$100 reais é {quantidadeDinheiro}.')
    valorSaque = valorSaque - quantidadeDinheiro * 100

if valorSaque < 50:
    print(f'A quantidade de notas de R$50 reais é 0')
else:
    quantidadeDinheiro = valorSaque // 50 # // divide o número por inteiro
    print(f'A quantidade de notas de R$50 reais é {quantidadeDinheiro}.')
    valorSaque = valorSaque - quantidadeDinheiro * 50
if valorSaque < 20:
    print(f'A quantidade de notas de R$20 reais é 0')
else:
    quantidadeDinheiro = valorSaque // 20
    print(f'A quantidade de notas de R$20 reais é {quantidadeDinheiro}.')
    valorSaque = valorSaque - quantidadeDinheiro * 20
if valorSaque < 10:
    print(f'A quantidade de notas de R$10 reais é 0')
else:
    quantidadeDinheiro = valorSaque // 10
    print(f'A quantidade de notas de R$10 reais é {quantidadeDinheiro}.')
    valorSaque = valorSaque - quantidadeDinheiro * 10
if valorSaque < 5:
    print(f'A quantidade de notas de R$5 reais é 0')
else:
    quantidadeDinheiro = valorSaque // 5
    print(f'A quantidade de notas de R$5 reais é {quantidadeDinheiro}.')
    valorSaque = valorSaque - quantidadeDinheiro * 5
if valorSaque < 1:
    print(f'A quantidade de notas de R$1 reais é 0')
else:
    quantidadeDinheiro = valorSaque // 1
    print(f'A quantidade de notas de R$1 reais é {quantidadeDinheiro}.')
    valorSaque = valorSaque - quantidadeDinheiro * 1


