from random import randint
from time import sleep
lista = []
jogos = []
qntd = int(input('Digite quantos jogos você quer: '))
total = 1
while total <= qntd:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6: 
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'Os números sorteados foram {lista}')
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(2)