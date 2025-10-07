import random, time
num = int(input('quantas vezes voce quer apostar?? '))
for i in range(0, num):
    print(f'numero da aposta {i+1}:', end=" ")
    bet = random.sample(range(1, 61), 6)
    print(sorted(bet))
    time.sleep(2)