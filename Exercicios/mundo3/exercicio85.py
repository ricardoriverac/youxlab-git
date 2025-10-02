lista = []
lista_pares = []
lista_impares = []

for valores in range(7):
    resposta = int(input(f"Digite o {valores+1}ª numero: "))
    if valores % 2 == 0:
        lista_pares.append(valores)
    else:
        lista_impares.append(valores)
lista.append(lista_pares, lista_impares)
lista_pares.sort()
lista_impares.sort()
print("Números pares:", lista)
print("Números ímpares:", lista)
    