import random
print ("VAMOS JOGAR PEDRA, PAPEL E TESOURA!")
computador = int(input("Considere:\n número 1 = PEDRA\n número 2 = PAPEL\n número 3 = TESOURA\nAgora, digite sua escolha: "))
jogador = random.randint(1,3)
print (jogador)
if computador == jogador:
    print ("EMPATE")
elif (computador == 1 and jogador == 2) or (computador == 2 and jogador == 3) or (computador == 3 and jogador == 1):
    print ("VOCÊ PERDEU!")
else:
    print ("VOCÊ GANHOU")