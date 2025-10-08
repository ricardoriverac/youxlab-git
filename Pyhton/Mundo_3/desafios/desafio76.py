listagem = ('Achocolatado', '1.50', 'Bolo', '5.00', 'Cenoura', '4.30', 'Feijão', '13.00', 'Molho de tomate', '6.20',
            'Maionese', '7.99', 'Salgadinho', '3.50', 'Refrigerante', '4,00')

print('='*25)
print('{:^25}'.format('LISTAGEM DE PREÇOS'))
print('='*25)


for posição in range(0, len(listagem), 2): 
    print(f'{listagem[posição]:.<76}', 'R$', f'{listagem[posição+1]:>10}')
print('-'*25)