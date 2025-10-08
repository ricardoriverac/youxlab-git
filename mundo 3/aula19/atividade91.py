from random import randint
jogador1 = randint(0,6)
jogador2 = randint(0,6)
jogador3 = randint(0,6)
jogador4 = randint(0,6)

diciorario = {"jogador1": jogador1,"jogador2":jogador2,"jogador3":jogador3,"jogador4":jogador4}
diciorario_odernado = sorted(diciorario.items(), key=lambda item: item[1], reverse=True )
print(diciorario_odernado)
n = 0
for jogador, pontuacao in diciorario_odernado:
    n += 1
    print(f"{jogador} ficou em {n}, tirou {pontuacao}")
    
