termo = int(input("digite o primeiro termo: "))
razao = int(input("digite uma razao:")) 
c = 1
while c < 11:
    print(f"{termo}")
    termo += razao
    c += 1 
print("PAUSA") 
mais = int(input(" quantos termos voce que a mais? "))  
while mais > 0:
    c = 0
    while c < mais:
        print(termo)
        termo += razao
        c += 1
    mais = int(input(" quantos termos voce que a mais? "))
