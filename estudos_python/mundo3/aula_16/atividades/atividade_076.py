'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus
respectivos preços, na sequência. No final, mostre uma listagem de 
preços, organizando os dados em forma tabular.
'''

#Resposta
b = 0
listagem = (
    'Pizza', 25.00,
    'Hambúrguer', 19.00,
    'Lasanha', 27.00,
    'Coxinha', 7.00,
    'Pastel', 15.00,
    'Sorvete', 9.00,
    'Tapioca', 13.00,
    'Empada', 11.00,
    'Bolo', 21.00,
    'Pão de queijo', 5.00
)

print('LISTA DE PREÇOS:\n')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(listagem[pos], end= '')
    
    else:
         print(f'   R${listagem[pos]}')

