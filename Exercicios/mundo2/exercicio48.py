soma=0
for impares in range(1,501,2):
    if impares%3==0:
        print(impares)
        soma+=impares
print(f"A soma de todos os numeros impares sao: {soma}")