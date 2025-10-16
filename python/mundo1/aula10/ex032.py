#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

import calendar
calend = int(input('Digite o ano para verificar se ele é bissexto: '))
if calendar.isleap(calend):
    print(f'{calend} é um ano bissexto.')
else:
    print(f'{calend} não é um ano bissexto.')
