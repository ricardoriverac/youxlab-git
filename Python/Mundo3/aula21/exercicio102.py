def fatorial(numero, show=False):
    """
    -> Calcula o Fatorial de um numero.
    :param numero: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um numero n.
    """
    f = 1
    for c in range (numero, 0, -1):
        if show:
            print(c, end='')
        else:
            print(' = ', end='')
        f *= c
    return f

print(fatorial(5, show=True))