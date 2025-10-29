from time import sleep
from random import randint
def sorteia(lista):
    for cont in range(0,5):
        numero = randint(1,10)
        lista.append(randint(1,10))
        print(f'{numeros}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO')





numeros = list()
sorteia(numeros)
print(numeros)