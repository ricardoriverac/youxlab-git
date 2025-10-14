
def contadorMaior(*num):
    maior=0
    print('-' * 5, "Analisando os valores passados", '-' * 5)
    for v in num:
        if v > maior:
            maior=v
    print(f'{num} Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior}')


contadorMaior(2, 9, 4, 5, 7, 1)
contadorMaior(4,7,0)
contadorMaior(6)
contadorMaior()