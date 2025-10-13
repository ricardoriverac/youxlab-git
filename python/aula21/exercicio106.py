def ajuda(txt):
    duvida = ' '
    while True:
        duvida = str(input(txt))
        help(duvida)
        resp = str(input('Quer continuar? [S/N] '))
        if resp in 'Nn':
            break
        
v1 = ajuda('Digite aqui: ')
print(v1)