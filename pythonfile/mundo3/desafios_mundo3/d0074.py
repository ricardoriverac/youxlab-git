import random
numeros = menor = 0
numeros = ()
print('Os numeros sorteados foram ')

for c in range(0, 5):
    numeroAleatorio = random.randint(0, 100)
    numeros += (numeroAleatorio,)
    print(numeroAleatorio)
    if c == 0:
        maior = menor = numeroAleatorio
    else:
        if numeroAleatorio > maior:
            maior = numeroAleatorio
        elif numeroAleatorio < menor:
            menor = numeroAleatorio


print(f'O maior é {maior} e o menor é {menor}')
print(f'numeros completos {numeros}')