def aumentar(preco = 0, taxa=0, formato=False):
    '''
    >> Calcula o aumento de um determinado preço, 
    retornando o resultado com ou sem formatação.
    :param preco: o preço que se quer reajustar.
    :param taxa: qual é a porcentagem do aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    '''
    result = preco + (preco * taxa/100)
    return result if format is False else moeda(result)

def diminuir(preco = 0, taxa = 0, formato=False):
    result = preco - (preco * taxa/100)
    return result if formato is False else moeda(result)

def dobro(preco = 0, formato=False):
    result = preco * 2
    return result if formato is False else moeda(result)

def metade(preco = 0, formato=False):
    result = preco / 2
    return result if formato is False else moeda(result)

def moeda(preco = 0, real=  'R$'):
    return f'{real}{preco:.2f}'.replace('.', ',')

def resumo(preco=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-'*30)