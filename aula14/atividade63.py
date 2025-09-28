cont = 0 
penultimo = 0
ultimo = 1
numero = int(input("quantos termos voce que mostra: ")) 
while cont <= numero:
    t3 = penultimo + ultimo
    penultimo = ultimo
    ultimo = t3
    cont += 1 
    print(ultimo) 
print("fim")     