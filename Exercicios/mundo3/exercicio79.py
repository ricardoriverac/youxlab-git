lista = []

for numero in range(5):
    valor = int(input(f"Digite o {numero+1}ª valor: "))
    lista += [valor,]
lista.sort()
print(f"Sua lista é {lista}")