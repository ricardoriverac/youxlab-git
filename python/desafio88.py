from random import randint
from time import sleep
print('-' * 40)
print('        JOGA NA MEGA SENA        ')
print('-' * 40)
jogos = []
quant = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(quant):
    jogo = []
    while len(jogo) < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    jogos.append(jogo)
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, lista in enumerate(jogos):
    print(f'Jogo {i+1}: {lista}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
