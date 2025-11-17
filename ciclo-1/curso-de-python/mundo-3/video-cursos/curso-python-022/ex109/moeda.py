def aumentar(a=0, b=0, formato=False):
    resultado = a + (a * b / 100)
    return resultado if formato is False else reais(resultado)

def diminuir(a=0, b=0, formato=False):
    resultado = a - (a * b / 100)
    return resultado if formato is False else reais(resultado)

def dobro(a=0, formato=False):
    resultado = a * 2
    return resultado if formato is False else reais(resultado)

def metade(a=0, formato=False):
    resultado = a / 2
    return resultado if formato is False else reais(resultado)

def reais(preco=0, simbolo='R$'):
    return f'{simbolo}{preco:>.2f}'.replace('.', ',')