menorPeso = 0
maiorPeso = 0

for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))

    if c == 1:
        maiorPeso = peso
        menorPeso = peso

    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
        menorPeso = peso

print(f'A pessoa mais pesada tem {maiorPeso} Kg.')
print(f'A pessoa mais leve tem {menorPeso} Kg.')