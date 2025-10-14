#gerar numero aleatorio
from random import randint
#adicionar pausa
from time import sleep

quantidade = int(input('Quantos jogos e pra sortear? '))
print( f'sorteando {quantidade} jogos')

for c in range(1, quantidade + 1):
    #amarzenar os numeros unicos
    jogo = set()
    while len(jogo) < 6:

        jogo.add(randint(1, 60))
    print(f'Jogo {c}: {sorted(jogo)}')

print('BOA SORTE!')