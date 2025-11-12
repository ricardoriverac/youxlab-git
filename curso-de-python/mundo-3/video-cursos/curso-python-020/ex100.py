from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 números...')
    for count in range(0, 5):
        numerosAleatorios = randint(1, 10)
        lista.append(numerosAleatorios)
        print(f'{numerosAleatorios}', end=' ', flush=True)
        sleep(0.7)

def somaPar(lista):
    soma = 0
    for numeros in lista:
        if numeros % 2 == 0:
            soma += numeros
    print(f'A soma de todos os números pares é {soma}')

listaNumerosAleatorios = []
sorteia(listaNumerosAleatorios)
print()
somaPar(listaNumerosAleatorios)