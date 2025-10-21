import random 


def sorteia(lista_numeros):
    for i in range(5):   
        lista_numeros.append(random.randint(1,10))
    print(lista_numeros)    
            

def somaPar(lista_numeros):
    soma=0
    for i in lista_numeros:
        if i % 2 == 0:
            soma += i
    print(f'Os numeros pares somados no total da {soma}')


numeros=list()
sorteia(numeros)
somaPar(numeros)