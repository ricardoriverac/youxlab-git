pares = []
impares = []
#lista para os numeros pares e impares
numeros = [pares, impares]
#lista com as duas listas dentro / uma lista aninhada
for c in range(0, 7):
    numero = int(input(f'Digite o {c + 1}º valor: '))
    #pegando 7 números da pessoa/ coletando
    if numero % 2 == 0:
        pares.append(numero)
        #se for par vai pra lista de números pares
    else:
        impares.append(numero)
        # se for impar va pra lista de numeros impares
pares.sort() #organiza os pares do menor pro maior
impares.sort() #organiza os impares do menor pro maior
#colocando os numeros em ordem.
print(f'numeros pares: {numeros[0]}') #numeros pares / lista
print(f'numeros ímpares: {numeros[1]}') #numeros impares / lista
#resultados