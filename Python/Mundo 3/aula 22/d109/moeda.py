def aumentar(preco = 0, taxa=0, formato=False):
    result = preco + (preco * taxa/100)
    return result if format is False else moeda(result)

def diminuir(preco = 0, taxa = 0, formato=False):
    result = preco - (preco * taxa/100)
    return result if formato is False else moeda(result)

def dobro(preco = 0, formato=False):
    result = preco * 2
    return result if formato is False else moeda(result)

def metade(preco = 0, formato=False):
    result = preco / 2
    return result if formato is False else moeda(result)

def moeda(preco = 0, real=  'R$'):
    return f'{real}{preco:.2f}'.replace('.', ',')
