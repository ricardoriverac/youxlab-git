# # Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# # O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
# # cadastrando tudo em uma lista composta.

from random import randint
print('-' * 70)
print('                              MEGA SENA                          ')
print('-' * 70)

jogosmega =[]
jogo=[]
quantidadejogos=int(input('Digite um número:'))
for j in range(quantidadejogos):
    jogo=[]
    while len(jogo)<6:
        numero =randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogo.sort()
    jogosmega.append(jogo)

print('\n=== Palpites Gerados ===')
for i, jogo in enumerate(jogosmega):
    print(f'Jogo {i+1}: {jogo}')
























