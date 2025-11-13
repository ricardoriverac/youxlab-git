def aumentar(a, b): 
    resultado = a + (a * b / 100)
    return resultado

def diminuir(a, b):
    resultado = a - (a * b / 100)
    return resultado 

def dobro (a):
    resultado = a * 2
    return resultado

def metade(a):
    resultado = a / 2
    return resultado

def reais(dinheiro):
    resultado = f'R${dinheiro}'.replace('.', ',')
    return resultado