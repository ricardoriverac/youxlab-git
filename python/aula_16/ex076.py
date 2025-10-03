'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

produtos = [
    ("Arroz", 5.99),
    ("Feijão", 6.49),
    ("Macarrão", 3.29),
    ("Óleo de soja", 7.89),
    ("Açúcar", 4.59)
]
print('--'*30)
print('LISTAGEM DE PREÇO')
print('--'*30)
for produto in produtos:
    print(produto)
print('--'*30)
