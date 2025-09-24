import random
tente = int(input("adivinhe o numero que estou pensando entre 0 a 10: "))
o = 0
p = 10
numero_escolhido = random.randint(o,p)
while tente != numero_escolhido:
    if tente < o or tente > p:
        print("digtou um numero fora do intervalo")
    else:
        print("voce errou ")    
    tente = int(input("adivinhe o numero que estou pensando entre 0 a 10: "))
print(f"o numero escolhido foi {numero_escolhido}")

