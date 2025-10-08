soma = 0
for numero in range(1,500,2):
    if numero % 3== 0:
        print(numero)
        soma += numero
print(f'A soma de todos os numeros impares são {soma}')