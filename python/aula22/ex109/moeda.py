#MÓDULO:

def dobro(n=0, formato=False):
    dobro = n * 2
    return dobro if formato is False else moeda(dobro)

def metade(n=0, formato=False):
    metade = n / 2
    return metade if formato is False else moeda(metade)

def aumentar (n=0, p=0,  formato=False):
    porc = (n * 10) / 100
    valor = n + porc
    return valor if formato is False else moeda(valor)

def diminuir (n=0, p=0, formato=False):
    porc = (n * 10) / 100
    valor = n - porc
    return valor if formato is False else moeda(valor)

def moeda(p = 0, moeda = 'R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')