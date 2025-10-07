listagem = ('Pão', '1.50', 'Macarrão', '5.00', 'Leite', '5.90', 'Açúcar', '7.00', 'Arroz', '14.20',
            'Feijão', '9.99', 'Molho', '3.92', 'Refrigerante', '6,50', 'Manteiga', '4.90')

print('^'*25)
print('{:^25}'.format('LISTAGEM DE PREÇOS'))
print('^'*25)


for posição in range(0, len(listagem), 2): 
    print(f'{listagem[posição]:.<76}', 'R$', f'{listagem[posição+1]:>10}')
print('-'*25)
 