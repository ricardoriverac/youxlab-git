'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o 
usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 
'''

#Resposta

nome_produto = 0
preco_produto = 0
deseja_continua = 0
soma = 0
preco_mais_1000 = 0
menor = 10000000000000
nome_produtomaisbarato = 0

while True:
    nome_produto = str(input('Digite o nome do produto: '))
    preco_produto = float(input('Digite o preço do preoduto: '))
    deseja_continua = str(input('Deseja continuar[s/n]: ')).lower()


    if preco_produto < 1000:
        preco_mais_1000 =+ 1 

    preco_produto += soma
    soma = preco_produto


    if preco_produto < menor:
        menor = preco_produto
        nome_produtomaisbarato = nome_produto

    
    if deseja_continua == 'n' or deseja_continua != 's':
        break

print(f'O nome do produto mais barato e {nome_produtomaisbarato} e o seu valor e {menor}')
print(f'A quantidade de produtos com o valor mais de 1000R$ e {preco_mais_1000}')
print(f'E a soma de todos os produtos e {soma}')