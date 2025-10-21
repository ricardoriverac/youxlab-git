tabela = ('lapis.............R$1.75','borracha..........R$2.00','Caderno...........R$15.90','Estojo............R$25.00','Transferidor......R$4.20',
'Compasso..........R$9.99', 'Mochila...........R$120.32','Canetas...........R$22.30', 'Livro.............R$34.90')
print('-'*40)
print(' ------LISTAGEM DE PRODUTOS------ ')
print('-'*40)
for c in range (0,len(tabela)):
 print(f'{tabela[c]}')
print('-'*40)