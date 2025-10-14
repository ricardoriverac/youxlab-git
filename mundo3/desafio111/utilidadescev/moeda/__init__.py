def aumentar(preco, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)
    

def diminuir(preco, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco,formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxa=0):
    print('=' * 30)
    print('RESUMO'.center(30))
    print('=' * 30)
    print(f'Preço fornecido: {moeda(preco)}')
    print('=' * 30)
    print(f'Dobro:\t\t{dobro(preco, True)}')
    print(f'Metade:\t\t{metade(preco, True)}')
    print(f'Aumento:\t{aumentar(preco, taxa, True)}')
    print(f'Desconto:\t{diminuir(preco, taxa, True)}')
    print('=' * 30) 