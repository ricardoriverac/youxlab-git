def fatorial(numero, show=False):
    """
    calcule o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n.
    """ 
    f =1 
    for c in range(numero,0,-1):
        if show:
            print('c', end=' ')
            if c>1:
             print(f'{c} x', end=' ')
            else:
               print('=', end=' ')
        f *= c
    return f

print(fatorial(5, show=True))
help(fatorial)