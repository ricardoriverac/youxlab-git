numeros = []
for c in range (5):
    numeros.append(int(input('Escreva um número:')))

maiornumero = max(numeros)
menornumero = min(numeros)

print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {maiornumero} nas posições {numeros.index(maiornumero)}')
print(f'O menor valor digitado foi {menornumero} nas posições {numeros.index(menornumero)}')