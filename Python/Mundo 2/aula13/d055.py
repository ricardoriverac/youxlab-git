maior = 0
menor = 0 
for pessoas in range(1, 6):
    peso = float(input(f'Peso da {pessoas}º pessoa: '))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso digitado foi de {maior}Kg.')
print(f'O menor peso digitado foi de {menor}Kg.')
