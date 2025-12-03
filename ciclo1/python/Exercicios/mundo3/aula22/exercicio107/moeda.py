def aumentar (valor = 0, taxa = 0):
    preco = valor + (valor*taxa /100)
    return preco
def diminuir (valor = 0, taxa = 0, formato = False):
    preco = valor - (valor*taxa / 100)
    return preco

def dobro (valor = 0, formato =False):
    preco = valor * 2
    return preco 

def metade (valor = 0, formato = False):
    preco = valor / 2
    return preco