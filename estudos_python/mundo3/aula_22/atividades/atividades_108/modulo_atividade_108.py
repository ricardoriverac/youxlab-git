def metade(metade_valor):
    r = metade_valor / 2
    return r


def dobro(dobro):
    r = dobro * 2
    return r 

def diminuir(diminuir):
    r = diminuir * (1 -  10 / 100)
    return r

def aumentar(aumentar):
    r = aumentar * (1 + 10 / 100)
    return r

def moeda (preço=0, moeda='R$'):
    return f'(moeda) (preço)'.replace('.',',')