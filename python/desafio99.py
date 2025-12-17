from time import sleep
def maior(*núm):
    print('-=' * 20)
    print('Analisando os valores passados...')
    sleep(0.5)
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
    print(f'→ Foram informados {len(núm)} valores ao todo.')
    if len(núm) == 0:
        print('Nenhum valor foi informado.')
    else:
        print(f'O maior valor informado foi {max(núm)}.')
    print('-=' * 20)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
