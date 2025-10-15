def maior(*numero):
    print('---' * 15)
    print('Analisando os valores passados...')
    conta = 0
    for c in numero:
        conta += 1
    if conta > 0:
        m = max(numero)
    else:
        m = 0
    print(f'{numero} Foram informados {conta} valores ao todo.')
    print(f'O maior valor informado foi {m}.')


maior(2, 4, 6, 8, 12)
maior(50, 4, 0)
maior(6, 9)
maior(8)
maior()