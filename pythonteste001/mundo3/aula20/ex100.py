from random import randint

def sortear(lista):
    print('Sorteando 5 números da lista: ', end= '')
    for contagem in range(0, 5):
        numero = randint(1, 10)
        lista.append(numero)
        print(f'{numero} ', end= '', flush=True)
    print()


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Ao somar os números pares de {lista},temos {soma}')

numeros = list()
sortear(numeros)
somaPar(numeros)