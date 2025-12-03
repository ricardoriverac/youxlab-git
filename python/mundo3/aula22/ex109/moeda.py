def metade(n, formatar=False):
    calculo_metade = n / 2
    return moeda(calculo_metade) if formatar else calculo_metade

def dobro(n, formatar=False):
    res = n * 2
    return moeda(res) if formatar else res

def aumentar(n, taxa, formatar=False):
    novo_valor = n * 1.1
    return moeda(novo_valor) if formatar else novo_valor

def diminuir(n, taxa, formatar=False):
    novo_valor = n * 0.87
    return moeda(novo_valor) if formatar else novo_valor

def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')
