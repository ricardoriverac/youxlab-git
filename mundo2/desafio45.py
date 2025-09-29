import random
print ("VAMOS JOGAR PEDRA, PAPEL E TESOURA!")
jogador = int(input("Considere:\n1 = PEDRA\n2 = PAPEL\n3 = TESOURA\nAgora, digite sua escolha: "))
bot = random.randint(1,3)
print (bot)
if jogador == bot:
    print ("EMPATE")
elif (jogador == 1 and bot == 2) or (jogador == 2 and bot == 3) or (jogador == 3 and bot == 1):
    print ("VOCÊ PERDEU!")
else:
    print ("VOCÊ GANHOU")