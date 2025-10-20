def aumentar(preco, taxa):
    result = preco + (preco * taxa/100)
    return result

def diminuir(preco, taxa):
    result = preco - (preco * taxa/100)
    return result

def dobro(preco):
    result = preco * 2
    return result

def metade(preco):
    result = preco / 2
    return result