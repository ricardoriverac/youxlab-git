def aumentar(preço=0, taxa=0, formata=False):
    """
    -> Calcula o aumento de um determinado preço.
    :param preço: valor original
    :param taxa: porcentagem de aumento
    :param formata: (opcional) se True, retorna o valor formatado em moeda
    :return: novo valor com o aumento aplicado
    """
    res = preço + (preço * taxa / 100)
    return res if not formata else moeda(res)

def diminuir(preço=0, taxa=0, formata=False):
    """
    -> Calcula a redução de um determinado preço.
    :param preço: valor original
    :param taxa: porcentagem de redução
    :param formata: (opcional) se True, retorna o valor formatado em moeda
    :return: novo valor com o desconto aplicado
    """
    res = preço - (preço * taxa / 100)
    return res if not formata else moeda(res)

def dobro(preço=0, formata=False):
    """
    -> Retorna o dobro de um preço.
    :param preço: valor original
    :param formata: (opcional) se True, retorna o valor formatado em moeda
    :return: o dobro do preço
    """
    res = preço * 2
    return res if not formata else moeda(res)

def metade(preço=0, formata=False):
    """
    -> Retorna a metade de um preço.
    :param preço: valor original
    :param formata: (opcional) se True, retorna o valor formatado em moeda
    :return: a metade do preço
    """
    res = preço / 2
    return res if not formata else moeda(res)

def moeda(preço=0, moeda='R$'):
    """
    -> Formata um valor numérico como moeda.
    :param preço: valor numérico
    :param moeda: símbolo da moeda (padrão: 'R$')
    :return: string formatada, ex: 'R$1.234,56'
    """
    return f'{moeda}{preço:>.2f}'.replace('.', ',')