#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


import random
number_lista = []
quanti_nume = 5
for _ in range(quanti_nume):
    numero_aleatorio= random.randint(0,100)
    number_lista.append(numero_aleatorio)
number_tupla =tuple(number_lista)
print(f'Os números gerados e armazenados na tupla são: {number_tupla}')
print(f'O maior valor na tupla é: {max(number_tupla)}')
print(f'O menor valor na tupla é: {min(number_tupla)}')