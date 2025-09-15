import random
primeiro=str(input("Primeiro nome: "))
segundo=str(input("Segundo nome: "))
terceiro=str(input("Terceiro nome: "))
quarto=str(input("Quarto nome: "))
lista=[primeiro,segundo,terceiro,quarto]
random.shuffle(lista)
print("A ordem da apresentação será: ")
print(lista)