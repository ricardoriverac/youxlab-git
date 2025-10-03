from random import randint
import time
lista = []
print('-=' * 15)
print('    Joga na mega sena     ')
print('-=' * 15)
jogos = int(input('Quantos jogos voce quer que eu sorteie?: '))
total = count = 0
while total <jogos:
    total += 1
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count == 6:
            break
    lista.sort()
    print(f'{total}o jogo:', lista)
    time.sleep(1)
    lista.clear()
    count = 0
