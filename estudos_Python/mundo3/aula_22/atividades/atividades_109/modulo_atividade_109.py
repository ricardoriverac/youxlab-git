def metade(valor, formatado = False):
    valor = valor / 2
    if formatado == True:
        return moeda(valor).replace('.' , ',')
    else:
        return valor


def dobro(valor, formatado = False):
    valor = valor * 2
    if formatado == True:
        return moeda(valor).replace('.' , ',')
    else:
        return valor

def diminuir(valor, formatado = False, taxa = 10):
    valor = valor * (1 -  taxa / 100)
    if formatado == True:
        return moeda(valor).replace('.' , ',')
    else:
        return valor
        

def aumentar(valor, formatado = False, taxa = 10):
    valor = valor * (1 + taxa / 100)
    if formatado == True:
        return moeda(valor).replace('.' , ',')
    else:
        return valor

def moeda(formatacao_valor):
    return f'R${formatacao_valor:.2f}'.replace('.' , ',')
