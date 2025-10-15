def aumentar(n = 0, a = 0, formato = False):
    resp = n + (n*a/100)
    return resp if formato is False else moeda(resp)
def diminuir(n = 0, d = 0, formato = False):
    resp = n - (n*d/100)
    return resp if formato is False else moeda(resp)
def dobro(n = 0, formato = False):
    resp = n * 2
    return resp if not formato is False else moeda(resp)

def metade(num = 0, formato = False):
    resp = num/2
    return resp if not formato is False else moeda(resp)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')