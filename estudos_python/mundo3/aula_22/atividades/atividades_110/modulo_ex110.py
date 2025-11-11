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

def resumo(valor, taxa_aumentar, taxa_diminuir):
    dobro_preço = valor * 2
    metade_preço = valor / 2
    aumentar = valor * (1 + taxa_aumentar / 100)
    diminuir = valor * (1 - taxa_diminuir / 100)
    print('-' * 30)
    print('Resumo dos Dados')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{moeda(dobro_preço)}')
    print(f'A metade do preço: \t{moeda(metade_preço)}')
    print(f'{taxa_aumentar}% de aumento: \t{moeda(aumentar)}')
    print(f'{taxa_diminuir}% de redução: \t{moeda(diminuir)}')