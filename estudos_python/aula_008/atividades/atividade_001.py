'''
Crie um programa que leia um número
real qualquer pelo teclado e mostre
na tela a sua porção inteira 
'''

#Resposta 

import math

numero = float(input('Digite um número : '))

print(f'O número inteiro é {math.trunc(numero)}')
