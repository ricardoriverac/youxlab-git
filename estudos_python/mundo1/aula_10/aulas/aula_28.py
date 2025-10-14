'''
Escreva um programa que faça o computador "pensar" em um número 
inteiro entre 0 e 5 peça para o usuário tentar descobrir qual foi 
o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

#Resposta

from random import randint
numero_aleatorio = (randint(0, 5))
digite_o_valor = int(input('Digite um número de 0 a 5: '))

if numero_aleatorio == digite_o_valor :

    print('Você ACERTOU!!')
else:
    print('Você ERROU!!')
print('--FIM--')