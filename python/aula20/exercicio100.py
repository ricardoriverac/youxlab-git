from random import randint
def sorteia():
    pos = 0
    while pos <= 4:
        num = randint(1, 10)
        numeros.append(num)
        pos += 1
    print(numeros) 
def somaPar():
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(soma)

numeros = []
sorteia()
somaPar()
