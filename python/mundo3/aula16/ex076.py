#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência.No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('----SUPERMERCADO DA THATHA-----')
produtos_precos = ('Maça',2.55,'Desifetante',5.0,'Arroz',15.0,'Alface',8.99)
for prod in range(0, len(produtos_precos)):
    if prod % 2 == 0:
        print(f'{produtos_precos[prod]}')
    else:
        print(f'R${produtos_precos[prod]}')
print('TENHA UMA BOA COMPRA!!')