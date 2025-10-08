from time import sleep
def maior(*numero):

    if numero == ():
        print('- Parâmetros não informados.')
    else:
        for i in numero:
            print(i, end=' ')
            sleep(0.1)
        print(f'\nnumero- Foram imformados {len(numero)} valores.\nnumero'
              f'O maior valor é o {max(numero)}')
    


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()