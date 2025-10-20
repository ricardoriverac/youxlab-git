def leiaInt(msg):

    aceito = False
    valor = 1
    while True:
        n = str(input(msg))
        if n.isnumeric():# ele vai indicar se verdade ou mentira
            valor = int(n)
            aceito = True
        else:
            print('digite um numero inteiro valido')
        if aceito:
            break
    return valor
n = leiaInt('digite um numero: ')
print(f'voce acabou de digitar o numero: {n}')