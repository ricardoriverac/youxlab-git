numeros = [[], []]
numero = 0

for c in range(1, 8):
    numero = int(input(f'Digite o {c}º número: '))

    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

print('-' * 25)
numeros[0].sort()
print(f'Os números pares digitados são: \033[33m{numeros[0]}\033[m')

numeros[1].sort()
print(f'Os números ímpares digitados são: \033[33m{numeros[1]}\033[m')