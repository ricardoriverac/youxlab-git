import random
maior = menor = 0 
numeros = ()
print("Os numeros sorteados são ")

for c in range(0 , 5):
    numero_sorteado = random.randint(0, 100)
    numeros += (numero_sorteado,)
    print('-> ', numero_sorteado )
    if c == 0:
        maior = menor = numero_sorteado
    else:
        if numero_sorteado > maior:
            maior = numero_sorteado
        elif numero_sorteado < menor:
            menor = numero_sorteado

print(f"O maior numero é: {maior} e o menor é {menor}")
print(f"Numeros completos {numeros}")
            