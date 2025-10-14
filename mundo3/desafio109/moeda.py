def aumentar(preco, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else real(res)
    

def diminuir(preco, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else real(res)


def dobro(preco,formato=False):
    res = preco * 2
    return res if formato is False else real(res)


def metade(preco, formato=False):
    res = preco / 2
    return res if formato is False else real(res)


def real(preco=0, real='R$'):
    return f'{real}{preco:.2f}'.replace('.', ',')