import random
armazem=list()
num=0
usuario=int(input('Quantos jogos você quer que eu sorteio?  '))
for l in range (1, usuario+1):
    while len(armazem) < 6:
        num=random.randint(1,60)
        if num not in armazem:
            armazem.append(num)

         
    print(f'Jogo {l}: {sorted(armazem)}')
    armazem.clear()
            




        