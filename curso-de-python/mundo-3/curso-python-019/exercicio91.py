import random #gerar um numero aleatorio
jogadores = {}
for c in range(1, 5):
    computador = random.randint(1,10) #numero aleatorio
    jogadores[f'jogador {c}'] = computador #amarzenando o dicionario
    print(f'O jogador {c} tirou: ', computador)
contador = 1
for i in sorted(jogadores, key = jogadores.get, reverse=True):
    print(f" {contador}º", i, jogadores[i])#pra colocar 0 nos numerosº
    contador +=1
    
print("O vencedor é o que está em 1° lugar!")
    