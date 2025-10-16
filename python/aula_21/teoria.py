def contador(i, f, p):
    c = i 
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')

contador(2, 10, 2)



def contador(i, f, p):
    c = i 
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')

contador(0, 100, 10)





def contador(i, f, p):
    """
    -> FAz uma contagem e mostra na tela.
    :param i: início da conategem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i 
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')


help(contador)