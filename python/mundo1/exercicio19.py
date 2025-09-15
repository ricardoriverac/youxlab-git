import random
primeiro=str(input("Primeiro nome: "))
segundo=str(input("Segundo nome:"))
terceiro=str(input("Terceiro nome: "))
quarto=str(input("Quarto nome: "))
lista=[primeiro,segundo,terceiro,quarto]
escolhido=random.choice(lista)
print(f"O aluno escolhido foi {escolhido}")