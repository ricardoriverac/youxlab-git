maior = 0
menor = 0
for y in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(y)))
    if y == 1:
        maior = peso
        menor = peso
    else: 
        if peso > maior: 
            maior = peso
        if peso < menor:
            menor = peso 
print('O maior peso lido foi de {}Kg'.format(maior))
print('O manor peso lido foi de {}Kg'.format(menor))