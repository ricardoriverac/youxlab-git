import random
lista = []
perm = []
nc1 = int(input('Quantas vezes você deseja replicar? '))
nc = 0

while nc != nc1 :
    for ne in range (0, 6):
        num = list(range(1, 60))
        escolhido = random.choice(num)
        lista.append(escolhido)
    nc += 1
    perm.append(lista[:])
    lista.clear()

print (f'Os números são :{perm}')