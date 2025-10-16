def aumentar (valor = 0, taxa = 0):
    res = valor + (valor*taxa /100)
    return res

def diminuir (valor = 0, taxa = 0, formato = False):
    res = valor - (valor*taxa / 100)
    return res

def dobro (valor = 0, formato =False):
    res = valor * 2
    return res 

def metade (valor = 0, formato = False):
    res = valor / 2
    return res