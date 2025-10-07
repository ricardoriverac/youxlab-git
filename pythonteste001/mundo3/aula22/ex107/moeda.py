def aumentar(preco, taxa=0):
    res = preco + (preco * taxa / 100)
    return res
    

def diminuir(preco, taxa=0):
    res = preco - (preco * taxa / 100)
    return res


def dobro(preco):
    res = preco * 2
    return res


def metade(preco):
    res = preco / 2
    return res
