from time import sleep
def maior(*num):
    print('-='*30)
    print(f'Analisando os valores apresentados...')
    maior = count = 0
    for valor in num:
        print(f'{valor}', end=' ', flush = True)
        sleep(0.3)
        if count == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        count += 1
    print(f' Foram {count} valores apresentados.')
    print(f' O maior valor informado foi o {maior}.')
maior(1, 2, 3, 4, 5, 6)
maior(2, 1, 6, 4)