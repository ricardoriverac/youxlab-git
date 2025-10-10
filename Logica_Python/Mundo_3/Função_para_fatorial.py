def fatorial(num=1, show=False):
    """
    Calcula fatorial de um número
    :param num: Numero a ser calculado
    :param show: (opcional) True para mostrar a conta
    :return: O valor do fatorial
    """
    print('='*30)
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == True:
            print(f'{c}{" x" if c > 1 else " ="}', end=' ')
    return f


print(fatorial(5))