from time import sleep
def maior(*num):
    if num == ():
        print('- Parâmetros não informados.')
    else:
        for i in num:
            print(i, end=' ')
            sleep(0.1)
        print(f'\num- Foram imformados {len(num)} valores.\num'
              f'O maior valor é o {max(num)}')
    print('-' * 30)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()