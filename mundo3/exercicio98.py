def linha():
    print(f'_' * 20)
def contador():
    linha()
    print (f'Contagem de 1 a 10 de 1 em 1:')
    linha()
    print()
    print (list(range(1, 11)))
    print()
    linha()
    print (f'Contagem 10 a 0 de -2 em -2: ')
    linha()
    print()
    print (list(range(10, 0, -2)))
    print()
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    print (list(range(inicio, fim+passo, passo)))


contador()