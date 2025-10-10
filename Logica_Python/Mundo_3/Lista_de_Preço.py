listagem = ('Mochila' , 150.50,
            'Caderno' , 20.40,
            'Lápis' , 1.50,
            'Caneta' , 2.00 ,
            'Borracha' , 3.00)
print('-' * 30)
print('Listagem de preços')
print('-' * 30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')