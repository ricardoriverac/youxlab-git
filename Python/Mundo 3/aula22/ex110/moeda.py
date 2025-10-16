def aumentar(preco=0, taxa=0, formatar=False):
    """
    Aumenta um valor em uma determinada porcentagem.
    :param preco: O valor a ser ajustado.
    :param taxa: A porcentagem de aumento.
    :param formatar: Se True, formata o resultado como moeda.
    :return: O valor aumentado.
    """
    res = preco + (preco * taxa / 100)
    return res if formatar is False else moeda(res)

def diminuir(preco=0, taxa=0, formatar=False):
    """
    Diminui um valor em uma determinada porcentagem.
    :param preco: O valor a ser ajustado.
    :param taxa: A porcentagem de redução.
    :param formatar: Se True, formata o resultado como moeda.
    :return: O valor diminuído.
    """
    res = preco - (preco * taxa / 100)
    return res if formatar is False else moeda(res)

def dobro(preco=0, formatar=False):
    """
    Retorna o dobro de um valor.
    :param preco: O valor a ser duplicado.
    :param formatar: Se True, formata o resultado como moeda.
    :return: O dobro do valor.
    """
    res = preco * 2
    return moeda(res) if formatar else res

def metade(preco=0, formatar=False):
    """
    Retorna a metade de um valor.
    :param preco: O valor a ser dividido.
    :param formatar: Se True, formata o resultado como moeda.
    :return: A metade do valor.
    """
    res = preco / 2
    return moeda(res) if formatar else res

def moeda(preco=0, moeda='R$'):
    """
    Formata um valor como moeda.
    :param preco: O valor a ser formatado.
    :param moeda: O símbolo da moeda (padrão é 'R$').
    :return: O valor formatado.
    """
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco=0, taxaa=10, taxar=5):
    """
    Mostra um resumo das operações do módulo para um dado valor.
    :param preco: O valor base para as operações.
    :param aumento: A porcentagem de aumento.
    :param reducao: A porcentagem de redução.
    """
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-' * 30)

