soma = 0
for numero in range(1, 501):
    if numero % 2 != 0 and numero % 3 == 0:
        soma = soma + numero 

print(f"A soma dos números ímpares múltiplos de 3 no intervalo é: {soma}")