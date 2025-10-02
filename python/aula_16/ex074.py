'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, 
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint
numero = randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)
print(f'Foram sorteados os números: {numero}')
print(f'\nO maior número sorteado foi {max(numero)}')
print(f'O menor número sorteado foi {min(numero)}')