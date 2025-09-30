menor = 100
maior = 0
for c in range(0,5):
    peso = int(input(f'Digite o peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso é {maior} e o menor peso é {menor}.')