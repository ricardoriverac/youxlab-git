lista = []

for valores in range(5):
    numeros = int(input(f"Digite o {valores+1}ª valor: "))
    lista += [numeros,]
print(f"Os numeros listados foram: {lista}")
valor_maior = max(lista)
valor_menor = min(lista)
posicao_maior = []
posicao_menor = []
for valores, i in enumerate(lista):
    if i == valor_maior:
        posicao_maior.append(i)
    if i == valor_menor:
        posicao_menor.append(i)
print(f"A posição do maior numero é: {posicao_maior}")
print(f"E a posição do menor é: {posicao_menor}")

