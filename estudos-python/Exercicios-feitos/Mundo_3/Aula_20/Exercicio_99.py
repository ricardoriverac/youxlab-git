from time import sleep
def maior(* numero):
    contador = maior = 0
    print('\nAnalisando os valores passados')
    for valor in numero:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if contador==0:
            maior=valor
        else:
            if valor>maior:
                maior=valor
        contador+=1
        
    print(f'Foram informados {contador} valores ao todo!')
    if len(numero) > 0:
        print(f'O maior valor informado foi {maior}!')
    else:
        print('Nenhum valor foi informado!')
maior(2, 9, 4, 3, 5, 7)
maior(8, 9, 3)
maior(7, 3)
maior(5, 3, 8, 6)
maior()