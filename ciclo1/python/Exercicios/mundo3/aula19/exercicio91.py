import random

jogadores = dict()



for c in range(1, 5):
    computador=random.randint(1,10)
    jogadores[f'jogador{c}'] = computador
    print(f'O jogador{c} tirou: ', computador)
    
    
contador=1

for i in sorted(jogadores, key = jogadores.get, reverse=True):
    print(f"{contador}º", i, jogadores[i])
    contador +=1
    
print("O vencedor é o que está em 1° lugar!")
    

# print(jogadores)
# print('------------------------------------------------')
# print(ranking)

        