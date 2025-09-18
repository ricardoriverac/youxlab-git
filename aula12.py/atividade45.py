from random import randint
itens = ("PEDRA","PAPEL","TESOURA")
computador = randint(0,2)
print("-=*"*10)
print("JOGO DE PEDRA,PAPEL,TESOURA")
print("-=*"*10)
print(""" escolha uma das opçoes 
[0] pedra
[1] papel
[2] tesoura""")
jogada = int(input("qual e a sua jogada? "))
print("""JO
KEN
PO""")
print("-=" *14)
print(f"O COMPUTADOR ESCOLHEU {itens[computador]}")
print(f"O JOGADOR ESCOLHEU {itens[jogada]} ")
print("-=" *14)
if computador == 0: #computador jogou pedra
    if jogada == 0:
        print("EMPATE")
    elif jogada == 1:
        print("""JOGADOR GANHOU
COMPUTADOR PERDEU""")
    elif jogada == 2:
        print("COMPUTADOR VENCEU")
    else:
        print("JOGADA INVALIDA")                 

elif computador == 1: # computador jogou papel
    if jogada == 0:
        print("COMPUTADOR VENCEU")
    elif jogada == 1:
        print("EMPATE")
    elif jogada == 2:
        print("""JOGADOR GANHOU
COMPUTADOR PERDEU""")
    else:
        print("JOGADA INVALIDA")

elif computador == 2: # computador jogou tesoura 
    if jogada == 0:
        print("""JOGADOR VENCEU"
COMPUTADOR PERDEU""")
    elif jogada == 1:
        print("COMPUTADOR VENCEU")
    elif jogada == 2:
        print("EMPATE")
    else:
        print("JOGADA INVALIDA") 
