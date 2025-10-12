lista = ('Massa', 5.70, 'Molho de Tomate', 1.90, 'Muçarela', 7.89, 'Pepperoni', 6.49, 'Calabresa', 5.99, 'Milho Enlatado', 4.49, 'Orégano', 1.99, 'Sal', 2.39, 'Carne Moída', 8.29)

print('-' * 50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-' * 50)

for posicao in range(0, len(lista)):
    if posicao % 2 == 0:
        print(f'{lista[posicao]:.<40}', end='')
    else:
        print(f'R$ {lista[posicao]:>6.2f}')

print('-' * 50)