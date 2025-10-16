'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''


from time import sleep

def maior(*  num):
    maximo = 0
    print('-=' * 40)
    print(f'Analisando os valores passados...')
    for k, v in enumerate(num):
        print(v, end=' ')
        if k == 0:
            maximo = v
        else:
            if v > maximo:
                maximo = v
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor inserido foi {maximo}')


maior(5, 4, 7, 3, 1)
maior(8, 9, 2, 7)
maior(0, 6, 5)
maior(10, 9)
maior(1)