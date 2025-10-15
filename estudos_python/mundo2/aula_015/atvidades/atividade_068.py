'''CODIGO NÃO FINALIZADO'''

'''
 Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando 
 o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
'''

# Resposta

import random

numero_computador = random.randint(1, 10)
numero_pessoa = 0 
par_impar = 0
vitoria_consecutivas = 0

while True :
    numero_pessoa = int(input('Digite um número: '))
    par_impar = str(input('Par ou Impar: ').upper())

    soma_valores = numero_computador + numero_pessoa

     #par
    if par_impar == 'PAR' and soma_valores % 2 == 0:
        print(f'VOCÊ GANHOU!!!')
        vitoria_consecutivas += 1 

    elif par_impar == 'PAR' and soma_valores % 2 == 0:
        print('a')
    