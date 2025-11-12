#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
# usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

total = 0
mil = 0
cont = 0
menor = 0
continuar = 'S'
menor_preco = 0
while continuar == 'S':
    produto = str(input('Qual é o nome do produto: '))
    preco =float(input('Qual é o valor do produto: R$'))
    cont += 1
    total += preco
    barato = produto
    if preco > 1000:
        mil += 1
    if cont == 1 or preco < menor_preco:
        menor_preco = preco
        produto_mais_barato = produto
    continuar = input('Você deseja continuar: [S/N]').upper()
print(f'O total gasto na compra é de R${total}')
print(f'{mil} produto custa mais de R$1000.00')
print(f'O nome do produto mais barato é {produto_mais_barato}.')

