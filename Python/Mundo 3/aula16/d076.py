produtos = 'Leite----------R$ 6,00', 'Água-----------R$ 3,00', 'Frango---------R$47,00', 'Queijo---------R$ 7,00', 'Feijão---------R$24,00', 'Lápis----------R$ 1,00', 'Pêra-----------R$ 5,00', 'Pipa-----------R$ 0,50', 'Groselha-------R$17,90'
print('-'*40)
print('     LISTA DE PREÇOS     ')
print('-'*40)
for lista in range(0, len(produtos)):
    if lista % 2 == 0:
        print(f'{produtos[lista]}')
    else:
        print(f'{produtos[lista]}')
print('-'*40)