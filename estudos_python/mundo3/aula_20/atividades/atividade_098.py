'''
Faça um programa que tenha uma função chamada contador(), que 
receba três parâmetros: início, fim e passo. Seu programa tem 
que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''

#Reposta

from time import sleep

def contador(inicio, fim, passo):
    if inicio > fim:
        passo = -passo


    for c in range(inicio,fim, passo):
        sleep(0.5)
        print(c)
    print('Fim...')


print('de 1 até 10, de 1 em 1')
for c in range(1, 11):
    sleep(0.5)
    print(c)
print('Fim...')

print('\nde 10 até 0, de 2 em 2:')
for b in range(10, 0, -2):
    sleep(0.5)
    print(b)
print('Fim...')

print('\nContagem personalizada')
contador(int(input('Digite o início: ')), int(input('Digite o fim: ')), int(input('Digite o passo: ')))