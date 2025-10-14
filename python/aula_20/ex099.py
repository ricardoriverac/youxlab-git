'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

def maior(lista):
    if not lista:
        return None, None

print('==' * 20)

numeros = [0, 9,3, 2, 6, 5, 1, 10]

maior_ = max(numeros)
menor = min(numeros)


maior(maior_)
maior(menor)
print(maior_)
