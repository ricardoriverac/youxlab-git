def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial de n
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return f
num = int(input('Digite um número: '))
mostrar = str(input('Quer ver o cálculo? [S/N] ')).strip().upper()
if mostrar == 'S':
    print(fatorial(num, show=True))
else:
    print(fatorial(num))