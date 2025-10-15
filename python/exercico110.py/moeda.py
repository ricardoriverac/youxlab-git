def aumentar(preco, taxa, formatar=False):
    """
    Aumenta um valor em uma determinada porcentagem.
    :param preco: O valor a ser ajustado.
    :param taxa: A porcentagem de aumento.
    :param formatar: Se True, formata o resultado como moeda.
    :return: O valor aumentado.
    """
    res = preco + (preco * taxa / 100)
    return moeda(res) if formatar else res

def diminuir(preco, taxa, formatar=False):
    """
    Diminui um valor em uma determinada porcentagem.
    :param preco: O valor a ser ajustado.
    :param taxa: A porcentagem de redução.
    :param formatar: Se True, formata o resultado como moeda.
    :return: O valor diminuído.
    """
    res = preco - (preco * taxa / 100)
    return moeda(res) if formatar else res

def dobro(preco, formatar=False):
    """
    Retorna o dobro de um valor.
    :param preco: O valor a ser duplicado.
    :param formatar: Se True, formata o resultado como moeda.
    :return: O dobro do valor.
    """
    res = preco * 2
    return moeda(res) if formatar else res

def metade(preco, formatar=False):
    """
    Retorna a metade de um valor.
    :param preco: O valor a ser dividido.
    :param formatar: Se True, formata o resultado como moeda.
    :return: A metade do valor.
    """
    res = preco / 2
    return moeda(res) if formatar else res

def moeda(preco, moeda='R$'):
    """
    Formata um valor como moeda.
    :param preco: O valor a ser formatado.
    :param moeda: O símbolo da moeda (padrão é 'R$').
    :return: O valor formatado.
    """
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco, aumento=10, reducao=5):
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
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(preco, reducao, True)}')
    print('-' * 30)