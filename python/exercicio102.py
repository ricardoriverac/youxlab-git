def fatorial(num, show=False):
    f=1
    for c in range(num, 0, -1):
        f=c*f
        if show == True:
            print(f'{c} ', end='')
            if c != 1:
                print(f'x ', end='')
            else:
                print('= ', end='')

    print(f'{f}')


fatorial(5,True)
fatorial(7, True)
fatorial(4)
        