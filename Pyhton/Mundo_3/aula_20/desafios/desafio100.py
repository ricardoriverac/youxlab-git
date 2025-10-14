from random import randint
from time import sleep

def sorteia(lista):
    for c in range(0,5):
        
        numero = randint(1,10)
        lista.append(numero)
        print(f'{numero} ', end ='', flush=True)
        sleep(0.5)
    print('acabou')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares temos: {soma}')

numeros = list()
sorteia(numeros)
somaPar(numeros)