# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
# com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep
def maior(*numero):
    if numero == ():
        print('- Parâmetros não informados.')
    else:
        for i in numero:
            print(i, end=' ')
            sleep(1)
        print(f'\nForam informados {len(numero)} valores.\n'
              f'O maior valor é o {max(numero)}.')
maior(8, 9, 4, 5, 7, 1)
maior(6, 2, 0)
maior(3, 10)
maior(9)
maior()