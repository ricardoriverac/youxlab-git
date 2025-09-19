import random
print ("VAMOS JOGAR PEDRA, PAPEL E TESOURA!")
jogador = int(input("Considere:\n1 = PEDRA\n2 = PAPEL\n3 = TESOURA\nAgora, digite sua escolha: "))
bot = random.randint('pedra', 'tesoura', 'papel')
print (bot)
if jogador == bot:
    print ("EMPATE")
elif (jogador == 'pedra' and bot == 'tesoura') or (jogador == 'tesoura 'and bot == 'papel') or (jogador == 'papel' and bot == 'pedra'):
    print ("VOCÊ PERDEU!")
else:
    print ("VOCÊ GANHOU")
bot=print()