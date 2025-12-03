lista = []
digitados = 0
for numeros in range(4):
    resposta = int(input(f"Digite o {numeros+1}ª valor: "))
    digitados += 1
    lista += [resposta,]
print(f"Voce digitou {digitados} numeros!")
lista.sort(reverse=True)
print(f"Lista ordenada decrescentemente: {lista}")
