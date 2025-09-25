for peso in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(peso)))
    if peso == 1:
        maior = peso
        menor = peso
    else: 
        if peso > maior: 
            maior = peso
        if peso < menor:
            menor = peso 
print('O maior peso lido foi de {}Kg'.format(maior))

