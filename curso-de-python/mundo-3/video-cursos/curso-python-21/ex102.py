def fatorial(numero, show=False):
    inicioFatorial = 1
    for c in range(numero, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

        inicioFatorial *= c
    return inicioFatorial

#Código Principal
print(fatorial(12, True))