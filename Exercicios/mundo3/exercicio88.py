import random

lista_jogos = []
jogo = []
pessoa=int(input('quantos jogos serão gerados? '))

for i in range(pessoa):
    jogo = []
    for c in range(6):
        computador=random.randint(1,61)
        jogo.append(computador)
    lista_jogos.append(jogo)

for j in lista_jogos:
    print("*", end="")
    for n in j:
        if n != j[-1]:
            print(n, end=", ")
        else:
            print(n, end="")
    print("*")