def metade(pre):
    r = pre / 2
    return r


def dobro(pre):
    r = pre * 2
    return r


def aumentar(pre, taxa):
    r = pre + (pre * taxa/100)
    return r


def moeda(pre):
    return f'R${pre:.0f},00'