def fatorial(num = 1, show = False):
    #o false vai definir um valor nulo, ou opcional, para o parÂmetro show
    f = 1
    for c in range(num, 0, -1):
        if show:
    #aqui, vai permitir um laço de repetição se o parâmetro show for verdadeiro
            print(c, end = ' ')
            if c>1:
                print('x', end= ' ')
            else:
                print('=', end= ' ')
        f *= c
        
    return f

print(fatorial(5, True))