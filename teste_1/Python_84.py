lista = []
listaP = []
maior = menor = 0

while True:
    lista.append(str(input('Nome:')))
    lista.append(float(input('Peso:')))
    
    if len(listaP) == 0:
        maior = menor = lista[1]
    
    if lista[1] > maior:
        maior = lista[1]


    elif lista[1] < menor:
        menor = lista[1]


    listaP.append(lista[:])
    lista.clear()

    continuar = (input('Quer continuar?[S/N]:')).strip().upper()
    if continuar == 'N':
        break

print(f'\nVocê cadastrou {len(listaP)} pessoas.')


print(f'O maior peso registrado foi de {maior}Kg. Peso de ', end='')
for c in listaP:
    if c[1] == maior:
        print(f'{c[0]} ', end='')
print()


print(f'O menor peso registrado foi de {menor}Kg. Peso de ', end='')
for c in listaP:
    if c[1] == menor:
        print(f'{c[0]} ', end='')
print()
