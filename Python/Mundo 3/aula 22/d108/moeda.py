def aumentar(preco = 0, taxa = 0):
    result = preco + (preco * taxa/100)
    return result

def diminuir(preco = 0, taxa = 0):
    result = preco - (preco * taxa/100)
    return result

def dobro(preco = 0):
    result = preco * 2
    return result

def metade(preco = 0):
    result = preco / 2
    return result

def moeda(preco = 0, real = 'R$'):
    return f'{real}{preco:.2f}'.replace('.', ',')