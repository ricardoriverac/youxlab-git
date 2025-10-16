from random import randint
from time import sleep

print('jogo da mega sena')


quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
print( f'sorteando {quantidade} jogos')

for i in range(1, quantidade + 1):
    jogo = set()
    while len(jogo) < 6:
        jogo.add(randint(1, 60))
    print(f'Jogo {i}: {sorted(jogo)}')
    sleep(0.8)

print('< BOA SORTE! >')