lista = []
lista_pares = []
lista_impares = []
for numeros in range(4):
    resposta = int(input(f"Digite o {numeros+1}ª numero: "))
    lista.append(resposta)
    if resposta % 2 == 0:
        lista_pares.append(resposta)
    else:
        lista_impares.append(resposta)
print(f"Os valores de par é: {lista_pares}")
print(f"Os valores impares são : {lista_impares}")
print(f"Sua lista é: {lista}")