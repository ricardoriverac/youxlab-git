def maior(*numeros):
    print('Analisando os valores passados...')
    

    if len(numeros) == 0:
        print('Nenhum valor foi informado.')
        return

    for n in numeros:
        print(f'{n} ')
    print(f'→ Foram informados {len(numeros)} valores ao todo.')

    maior_valor = max(numeros)  
    print(f'O maior valor informado foi {maior_valor}.')
    print('-=' * 20)



maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()  