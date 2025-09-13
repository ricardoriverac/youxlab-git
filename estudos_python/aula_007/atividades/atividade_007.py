#Faça um algoritmo que leia o preço de um produto e mostre o seu preço, com 5% de desconto 

#Resposta 

preco_do_produto = int(input('Digite o preço do produto : '))
preco_com_desconto = ((preco_do_produto * 10) / 100)
desconto = (preco_do_produto - preco_com_desconto)

print(f'O preço do produto com 5% de desconto e {desconto}')