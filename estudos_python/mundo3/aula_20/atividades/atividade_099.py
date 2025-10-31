'''
Faça um programa que tenha uma função chamada maior(), que 
receba vários parâmetros com valores inteiros. Seu programa 
tem que analisar todos os valores e dizer qual deles é o maior.
'''

#Responda

from time import sleep
def maior(*mai):
    print(f'Foram passado {len(mai)} números, e o maior número foi {max(mai)}.')


maior(9, 1, 33 , 20 ,5 )
sleep(1)
maior(0, 23, 165, 34, 234, 76, 9)
sleep(1)
maior(54, 456, 23, 12, 98, 34, 87, 34, 5, 2) 
