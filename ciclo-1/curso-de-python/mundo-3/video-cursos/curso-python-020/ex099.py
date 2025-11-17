from time import sleep

def maior(* numero):
    count = maiorNumero = 0
    print('-' * 30)
    print('Analisando os números...')
    for numeros in numero:
        print(f'{numeros} ', end='', flush=True)
        sleep(0.7)
        if count == 0:
            maiorNumero = numeros
        else:
            if numeros > maiorNumero:
                maiorNumero = numeros
        count += 1
    print(f'Foram lidos no total {count} números.')
    print(f'O maior número analisado foi o número {maiorNumero}.')

#Programa Principal
maior(5, 2, 1, 7, 9, 10)
maior(3, 8, 0)
maior(6, 1)
maior(-1)