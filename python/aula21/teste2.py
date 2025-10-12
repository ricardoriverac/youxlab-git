def soma(a=0, b=0, c=0):
    """
    :param a: o primeior valor
    :param b: o segundo valor
    :param c: o terceiro valor
    ->função com objetivo de calcular uma soma entre três parâmetros, sendo eles 'a', 'b' e 'c'
    todos os três parâmetros são opcionais, determinados assim por atribuir um valor 0(nulo) para eles
    """
    s = a+b+c
    print(s)
soma(b = 2, a=4)