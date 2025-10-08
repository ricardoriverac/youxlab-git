from random import randint
from time import sleep
print('='*30)
print('-='*5, 'Megasena', '=-'*5)
print('='*30)
lista = []
palp = []
n = int(input('Quantos palpites quer gerar? '))
print(f'-=-=-= SORTEANDO {n} JOGOS =-=-=-')
for c in range(n):
    for p in range(6):
        num = randint(1, 60)
        while num in palp:
            num = randint(1, 60)
        palp.append(num)
    lista.append(palp[:])
    palp.clear()
for c in range(n):
    sleep(0.5)
    print(f'Jogo {c+1}: {sorted(lista[c])}')
print('-='*5, 'BOA SORTE', '=-'*5)