produtosPrecos = ('Lapiseira', 9.99, 'Caixa de leite', 5.50)
print('-'*20)
for pos in range(0, len(produtosPrecos)):
    if pos % 2 == 0:
        print(f'{produtosPrecos[pos]:.<30}', end='')
    else:
        print(f'{produtosPrecos[pos]:.>10}')
print('-'*20)
