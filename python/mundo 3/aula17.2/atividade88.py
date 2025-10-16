print("-="*20)
print(" MEGA SENA")
print("-="*20)
from random import randint
from time import sleep
jogos = []
numeros_sorteados = int(input("quantas rodadas voce quer: "))
for i in range(numeros_sorteados):
    jogo = []
    while len(jogo) < 6:
        num = randint(1,60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()       
    jogos.append(jogo) 
print("------  PALPITES GERADOS ------ ") 
for i, j in enumerate(jogos,1):
    print(f"jogo {i}: {j} ") 
    sleep(0.7)