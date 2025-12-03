lista = []

for numero in range(5):
    valor = int(input(f"Digite o {numero+1}ª valor: "))
    lista.append(valor)
lista_ordenada = sorted(lista)
print(f"Sua lista em ordem crescente é: {lista_ordenada}")
