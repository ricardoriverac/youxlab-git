import random
def sorteadorLista(lst):
    for c in range (0, 6):
        num=random.randint(1, 10)
        lista.append(num)
    print(f'Sorteando os valores da lista: {lista}')
def valoresPares(lst):
    somaPares=0
    for v in lista:
        if v % 2 == 0:
            somaPares+=v
    print(f'Somando os valores pares de {lista}, temos {somaPares}')


lista=[]
sorteadorLista(lista)
valoresPares(lista)