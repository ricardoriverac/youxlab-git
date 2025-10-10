from random import randint

maior = 0
menor = 0
numeros = ()
for n in range(0, 5):
    numerosAleatorios = randint(1, 11)
    if n == 0:
        maior=menor=numerosAleatorios
    else:
        if numerosAleatorios > maior:
            maior=numerosAleatorios
        if numerosAleatorios < menor:
            menor = numerosAleatorios
    numeros += (numerosAleatorios, )
print(f'o maior número entre eles é {maior} e o menor é {menor}')
print(numeros)