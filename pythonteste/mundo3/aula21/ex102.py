def fatorial(numero, show=False):
    fatorial = 1
    for contador in range(numero, 0, -1):
        if show:
            print(contador, end=' ')
            if contador > 1:
                print('x',end=' ')
            else:
                print('=',end=' ')
        fatorial *= contador
    return fatorial
    

print(fatorial(5, show=True))