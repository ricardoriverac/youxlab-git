from random import randint
from time import sleep
numeros = list()
pares = list()

def sort(lista):
    for c in range(0,10):
        numero = randint(1,9)
        lista.append(numero)
        if numero % 2 == 1:
            print(f'{numero} ',end='')
            sleep(0.1)
        if numero % 2 == 0:
            print(f'{numero}', end='')
            sleep(0.1)
            pares.append(numero)
    print(f' NÚMEROS PARES SORTEADOS: {pares}',end='')

def somapares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    print(f'\nA SOMA DOS PARES É = {soma}')

sort(numeros)
somapares(numeros)