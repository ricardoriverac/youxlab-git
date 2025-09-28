from math import trunc
numero = float(input('Digite um número com números decimais: '))
inteiro = trunc(numero)
print('A parte inteira de {} é {:.0f}'.format(numero, inteiro))