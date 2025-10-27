'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos 
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

#Resposta
import random

resultado_mega_sena = []
contador = 0
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
         11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
         21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
         41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
         51, 52, 53, 54, 55, 56, 57, 58, 59, 60]

print('''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
         TODOS OS NÚMEROS SORTEADOS DA MEGA-SENA
         -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=''')
quantidade_de_jogos_sorteado = int(input('Qual e a quantidade de jogos de você deseja sortear: '))
while True:
    contador += 1
    random.shuffle(lista)
    resultado_mega_sena.append(lista[:7])
    print(resultado_mega_sena)
    resultado_mega_sena.clear()

    if contador == quantidade_de_jogos_sorteado:
        break