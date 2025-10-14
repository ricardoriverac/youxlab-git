from time import sleep
def maior(* numero):
    contador = maior = 0
    print('\nAnalisando números. . . . ')
    for valor in numero:
        print(f'{valor} ')

        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador +=1
    print(f'Valores ao todo: {contador}')
    print(f'Maior valor: {maior}')

maior(3,2,1,4,5)
maior(2,3,9)
maior(1)
maior()