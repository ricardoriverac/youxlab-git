def fatorial(num = 1, show = False):
    fat = 1
    for i in range(num, 0, -1):
        fat = fat * i
        if show:
            print(f'{i}',end='')
            if i != 1:
                print(' x ',end='')
            else:
                print(' = ',end='')

    if show:
        print(fat)
    return fat 
numero = int(input('Digite um numero: '))
f = fatorial(numero)
print(f)