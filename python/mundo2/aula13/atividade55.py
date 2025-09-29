maior = 0
menor = 0
for c in range (0,5):
    peso = float(input("peso da pessoa:"))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso 
print(f"o maior peso das cinco pessoas foi {maior}kg ") 
print(f"o menor peso das cinco pessoas foi {menor} kg")                 