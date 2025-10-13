def aumentar(n = 0, a = 0):
    resp = n + (n*a/100)
    return resp
def diminuir(n = 0, d = 0):
    resp = n - (n*d/100)
    return resp
def dobro(n = 0):
    return n * 2

def metade(num = 0):
    return num/2

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')