#MÓDULO:

def aumentar(p = 0, taxa=0, format=false):
    res = p + (p * taxa/100)
    return res


def real (p = 0, real = 'R$'):
    return f'{real}{p: 2f}'.replace('.', ',')