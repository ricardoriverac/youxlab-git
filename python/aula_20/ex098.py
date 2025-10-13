'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''


from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)
    if inicio > fim:
        passo = -passo
        fim -= 2

    for c in range(inicio, fim+1, passo):
        print(c, end=' ')
        sleep(0.5)
    print()

contador(1, 10, 0)
contador(10, 0, 2)
contador(int(input('Informe o início: ')), int(input('Informe o fim: ')), int(input('Informe o passo: ')))
