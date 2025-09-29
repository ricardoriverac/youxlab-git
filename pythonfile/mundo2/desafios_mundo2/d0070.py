contadorPreço = 0
total_gasto = 0
preco = 0
menor_preco = 0
produto_barato = 0
produtos_1000 = 0
condição = 's'
while condição == 's': 
    produto = str(input('Qual o produto: '))
    preco = int(input('Qual o preço R$: '))
    condição = str(input('Deseja adicionar mais? [s/n]: '))
    total_gasto += preco

    if preco < menor_preco or contadorPreço == 0:
        menor_preco = preco
        produto_barato = produto

    if preco > 1000:
        produtos_1000 +=1
    
    contadorPreço +=1
print(f'O total gasto foi de {total_gasto}')
print(f'Há {produtos_1000} que custa mais de 1000')
print(f'O produto mais barato é {produto_barato}')