'''
Crie um programa que vai gerar cinco números aleatórios e colocar 
em uma tupla. Depois disso, mostre a listagem de números gerados 
e também indique o menor e o maior valor que estão na tupla.
'''

#Resposta

from random import randint
menor = 6
maior = 0
c = 0
lista_aleatoria = (randint(1, 5) , randint(1, 5) , randint(1, 5) , randint(1, 5) , randint(1, 5))

print(f'A lista; {lista_aleatoria}')
print(f'O maior número: {max(lista_aleatoria)}')
print(f'O menor número: {min(lista_aleatoria)}')