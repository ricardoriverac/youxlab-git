'''
Faça um programa que leia o ano de nascimento de um jovem e informe. 
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar.
se é a hora de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

#Resposta
from datetime import date

ano_de_nascimento = int(input('Digite o ano de seu nascimento: '))
ano = date