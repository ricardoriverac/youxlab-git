def aumentar(valor = 0, taxa = 0, formato =False):
    res = valor + (valor*taxa /100)
    return res if formato is False else moeda(res)

def diminuir(valor = 0, taxa = 0, formato = False):
    res = valor - (valor*taxa / 100)
    return res if formato is False else moeda(res)

def dobro(valor = 0, formato =False):
    res = valor * 2
    return res if not formato else moeda(res)

def metade(valor = 0, formato = False):
    res = valor / 2
    return res if not formato else moeda(res)

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: {moeda(preço)}')
    print(f'Dobro do preço: {dobro(preço, True)}')
    print(f'Metade do preço: {metade(preço, True)}')
    print(f'80% de aumento: {aumentar(preço,10,True)}')