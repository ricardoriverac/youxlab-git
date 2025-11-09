from time import sleep
from random import randint
def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for cont in range(0,5):
        numero = randint(1,11)
        numeros.append(numero)
        print(f'{numeros}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO')


def somaPar(lista):
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {numeros}, temos {soma}')
     
numeros = list()

sorteia(numeros)
somaPar(numeros)