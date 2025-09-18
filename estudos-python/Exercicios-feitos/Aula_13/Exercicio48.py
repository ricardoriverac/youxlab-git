soma = 0
contador = 0
for contagem in range(1, 501, 2):
    if (contagem % 3 == 0):
        contador = contador + 1
        soma = soma + contagem
print (f'A soma de todos os {contador} valores solicitados é {soma}!')