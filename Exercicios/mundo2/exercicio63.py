numero = int(input("Quantos termos você quer mostrar? "))
termo1 = 0
termo2 = 1
print("~"*30)
print(f"{termo1} -> {termo2}")
contador = 3

while contador <= numero:
    termo3 = termo1 + termo2
    print(f" -> {termo3}")
    termo1 = termo2
    termo2 = termo3
    contador += 1 