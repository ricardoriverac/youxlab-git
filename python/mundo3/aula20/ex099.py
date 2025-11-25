#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    maior = max(num)
    print(f'Analisamos os números {num} e o maior é {maior}.')
maior(9,8,2,4,1)
maior(20, 10,5, 2, 7)
maior(778, 209, 5, 11)
maior(56, 2656, 89,727)

