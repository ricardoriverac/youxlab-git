def forma():
    while True:
        resp = str(input('Digite um comando: '))
        print (f'{help(resp)}')
        perg = str(input('Você deseja continuar? [S/N]')).upper()
        if perg == 'N':
            print(' PROGRAMA ENCERRADO')
            break

forma()