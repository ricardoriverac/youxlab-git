def metade(metade_valor, mostrar_formatado=False):
    r = metade_valor / 2
    if mostrar_formatado == True:
        r = float(f'R${r:.2f}'.replace('.' , ','))
    return r


def dobro(dobro_valor):
    r = dobro * 2
    return r 

def diminuir(diminuir_valor):
    r = diminuir * (1 -  10 / 100)
    return r

def aumentar(aumentar_valor):
    r = aumentar * (1 + 10 / 100)
    return r

def formatação(formatacao_valor):
    r = float(f'R${formatacao_valor:.2f}'.replace('.' , ','))
    return r
