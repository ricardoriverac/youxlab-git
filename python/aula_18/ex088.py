'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.
'''

# imprimir:
# * 05,08,09,23,35,60 *
# * 08,13,24,26,36,48 *


from random import randint

quantidade_jogos = int(input('Quantos jogos serão gerados? '))
lista_jogos = []

for i in range(quantidade_jogos):
    jogo = []
    for n in range(6):
        numero = randint(1, 60)
        jogo.append(numero)
    lista_jogos.append(jogo)

print(lista_jogos)