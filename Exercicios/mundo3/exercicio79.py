lista = []

for numero in range(5):
    valor = int(input(f"Digite o {numero+1}ª valor: "))
    if valor not in lista:
        lista.append(valor)
    else:
        print("Este valor ja existe!")
lista.sort()
print(f"Sua lista em ordem crescente é: {lista}")
    