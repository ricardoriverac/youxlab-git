def maior(* numero):
    contagem = maior = 0
    for valor in numero:
        print(f'{valor}', end=' ', flush=True)
        if contagem == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contagem += 1
    print(f'Foram {contagem} números informados')
    print(f'O maior número foi {maior}')


#Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7,0)
maior(1, 2)
maior(6)
maior()
