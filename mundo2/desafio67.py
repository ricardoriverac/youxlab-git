while True:
    n = int(input('De qual número queres ver a tabuada [negativo para finalizar]: '))
    if n < 0:
        break
    c = 1
    print('-'*11)
    while c < 11:
        print(f'{n} * {c} = {n * c}')
        c += 1
    print('-'*11)
print('Finalizado')