def aumentar(preco=0, taxa=0, formato=False):
    res = preco * (1 + taxa / 100)
    return res if not formato else moeda(res)

def diminuir(preco=0, taxa=0, formato=False):
    res = preco * (1 - taxa / 100)
    return res if not formato else moeda(res)

def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)

def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)

def moeda(preco=0, simbolo='R$'):
    return f'{simbolo}{preco:>.2f}'.replace('.', ',')

def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO NUMERO')
    print('-' * 30)
    print(f'Preço analisado: {moeda(preco)}')
    print(f'Dobro do preço: {dobro(preco, True)}')
    print(f'Metade do preço: {metade(preco, True)}')
    print(f'{taxaa}% de aumento: {aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: {diminuir(preco, taxar, True)}')
    print('-' * 30)
