from random import randint
from time import sleep
lista = []
jogos = []
print('-'*30)
print('    JOGO DA MEGA SENA    ')
print('-'*30)
jogadas = int(input('-> ''Jogos para sortear? '))
total = 1
while total <= jogadas:
    contar = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contar += 1
        if contar >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-'*30)
print(f' SORTEANDO {jogadas} JOGOS: ')
for i, l in enumerate(jogos):
    print(f'-Jogo {i+1}: {l}.')
    sleep(1)
print('-'*30)
print('    --> BOA SORTE! <--')
print('-'*30)
