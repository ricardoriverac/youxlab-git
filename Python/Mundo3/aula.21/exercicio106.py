while True:
    comando = str(input('Digite uma Função ou Biblioteca: '))
    print(help(comando))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        print('Fim!')
        break