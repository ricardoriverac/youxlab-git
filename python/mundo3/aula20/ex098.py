#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três
# contagens através da função criada:


def contador(inicio, fim, passo):
    if passo > 0:
        for num in range(inicio, fim + 1, passo):
            print(num, end=' ')
    else:
        for num in range(inicio, fim - 1, passo):
            print(num, end=' ')
print('COMTAGEM 1: De 1 a 10.')
contador(1, 10 ,1)
print('\n')
print('CONTAGEM 2: De 10 até 0 de 2 em 2.')
contador(10, 0, -2)
print('\n')
print('Contagem 3: Personalizada.')
contador(1, 15, 2)





