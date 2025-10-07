def aumentar(preco, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(preco)
    

def diminuir(preco, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(preco)


def dobro(preco,formato=False):
    res = preco * 2
    return res if formato is False else moeda(preco)


def metade(preco, formato =False):
    res = preco / 2
    return res if formato is False else moeda(preco)


def moeda(preco=0, moeda='R$', format=False):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
