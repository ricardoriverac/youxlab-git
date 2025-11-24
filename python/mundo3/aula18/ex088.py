#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random
jogos = []
gerar = int(input('Quantos jogos você deseja gerar? '))
for i in range(gerar):
    jogo = []
    while len(jogo) < 6:
        num = random.randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    jogos.append(jogo)
print('Jogos gerados:')
for idx, j in enumerate(jogos, 1):
    print(f'Jogo {idx}: {j}')