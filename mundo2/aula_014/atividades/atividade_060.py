'''
Faça um programa que laia um número qualquer a mostre o seu fatorial.
Ex:
5 = 5x4x3x2x1 = 120
'''

#Resposta

from math import factorial
digite_um_numero = int(input('Digite um número para calcular o seu fatorial: '))
f = factorial(digite_um_numero)
digite_um_numero = digite_um_numero + 1
print(f)
print('\nResposta: ')
while digite_um_numero != 1 :
    digite_um_numero = digite_um_numero - 1
    print(digite_um_numero , end= ' * ' )
print(f'= {f}')

