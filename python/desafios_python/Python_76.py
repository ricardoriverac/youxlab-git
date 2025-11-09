print('-' * 30)
print('LISTAGEM DE PREÇOS')
print('-' * 30)

listagem = ('Lápis',1.50,'Borracha',2.00,'Caderno',15.00,'Estojo',25.00,'Transferidor',4.00,'Compasso',10.00,'Mochila',120.00,'Kit Canetas',22.00,'Livro',34.00)
for itens in range(0,len(listagem),2):
    print(f'{listagem[itens]}....R${listagem[itens+1]} ')



