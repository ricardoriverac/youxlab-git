def aumentar (valor = 0, taxa = 0, formato =False):
    preco = valor + (valor*taxa /100)
    return preco if formato is False else moeda(preco)

def diminuir (valor = 0, taxa = 0, formato = False):
    preco = valor - (valor*taxa / 100)
    return preco if formato is False else moeda(preco)

def dobro (valor = 0, formato =False):
    preco = valor * 2
    return preco if not formato else moeda(preco)

def metade (valor = 0, formato = False):
    preco = valor / 2
    return preco if not formato else moeda(preco)

def moeda (valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')