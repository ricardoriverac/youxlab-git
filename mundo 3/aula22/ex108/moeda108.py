def aumentar(preco=0, taxa=0):
    return preco * (1 + taxa / 100)


def diminuir(preco=0, taxa=0):
    return preco * (1 - taxa / 100)


def dobro(preco=0):
    return preco * 2


def metade(preco=0):
    return preco / 2


def moeda(preco=0, simbolo='R$'):
    return f'{simbolo}{preco:>.2f}'.replace('.', ',')
