'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcula o preço da passagem, cobrando R$0.50 por Km para viagens de
até 200Km e R$0.45 para viagens mais longas.
'''

#Resposta

from math import trunc

quantoskmvaiviajar = int(input('Digite a quantidade de Km vai percorrer: '))

if quantoskmvaiviajar < 200 :

    preco_longo = (trunc(quantoskmvaiviajar * 0.50))
    print(f'Esse e o preço da sua viagem: {preco_longo}R$')

else :

    preco_curto = (trunc(quantoskmvaiviajar * 0.45))
    print(f'Esse e o preço da sua viagem: {preco_curto}R$')
