#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
# e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

import random
numeros = []
def sorteia():
    print('Sorteando 5 números da lista: ')
for c in range(0,5):
    valor = random.randint(0,100)
    numeros.append(valor)
    print(f' {valor}')
def soma_par():
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
            print(f'A soma dos valores pares são: {soma}')
sorteia()
soma_par()
