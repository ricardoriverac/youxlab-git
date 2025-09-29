from random import randint
venceu = 0
while True:
    computador = randint(0,999)
    tipo = " "
    while tipo not in "PI":
         tipo = str(input("par ou impar? [P/I] ")).upper()  
    if tipo == "P":
         if computador % 2 == 0:
              print("voce venceu")
              venceu += 1
         else:
              print("voce perdeu")
              break
    elif tipo == "I":
        if computador % 2 == 1:
              print("voce venceu") 
              venceu += 1 
        else: 
             print("voce perdeu")  
             break 
    print("vamos jogar denovo...")    
print(f"voce venceu {venceu} vezes")    
                    