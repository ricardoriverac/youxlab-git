from random import randint
grupoNumeros = []
quantidade = int(input('Quantos valores vocÊ gostaria que fossem sorteados?'))
def sorteia(lst):
    for p in range(quantidade):
        grupoNumeros.append(randint(0, 100))
    print ('Sorteando os valores da lista:')
def somaPar(lst):
    soma = 0
    for s in grupoNumeros:
        if s % 2 == 0:
            soma += s
    print(f'Com os valores da lista: {grupoNumeros} temos {soma}')
sorteia(grupoNumeros)
somaPar(grupoNumeros)