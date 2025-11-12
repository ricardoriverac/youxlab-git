def aumentar(preço=0, taxa=0):
    """
    -> Calcula o aumento de um determinado preço, retornando o resultado.
    :param preço: valor original
    :param taxa: porcentagem de aumento
    :return: novo valor com o aumento aplicado
    """
    return preço + (preço * taxa / 100)
def diminuir(preço=0, taxa=0):
    """
    -> Calcula a redução de um determinado preço, retornando o resultado.
    :param preço: valor original
    :param taxa: porcentagem de redução
    :return: novo valor com o desconto aplicado
    """
    return preço - (preço * taxa / 100)
def dobro(preço=0):
    """
    -> Retorna o dobro de um preço.
    :param preço: valor original
    :return: o dobro do preço
    """
    return preço * 2

def metade(preço=0):
    """
    -> Retorna a metade de um preço.
    :param preço: valor original
    :return: a metade do preço
    """
    return preço / 2
def moeda(preço=0, moeda='R$'):
    """
    -> Formata um valor numérico como moeda.
    :param preço: valor numérico
    :param moeda: símbolo da moeda (padrão: 'R$')
    :return: string formatada, ex: 'R$1.234,56'
    """
    return f'{moeda}{preço:>.2f}'.replace('.', ',')