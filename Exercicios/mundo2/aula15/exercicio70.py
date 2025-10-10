resposta = "S"
total_gasto = 0
quantos_Produtos_Custa_Mais_De_1000 = 0
nome_produto_barato = 0
menor_preco = 0
contador = 0
while resposta == "S":
    nome = str(input("Qual o nome do produto?: "))
    preco = int(input("Qual o preço do produto?: R$ "))
    contador += 1
    total_gasto += preco
    if contador == 1:
        menor_preco = preco
        nome_produto_barato = nome
    else:
        if preco < menor_preco:
            menor_preco = preco
            nome_produto_barato = nome
    if preco > 1000:
        quantos_Produtos_Custa_Mais_De_1000 += 1
    resposta = input("deseja continuar ? [s/n]: ").upper()
print(f"O total gasto foi de {total_gasto}")
print(f"Ha {quantos_Produtos_Custa_Mais_De_1000} produto que custam mais de R$1000!")
print(f"O nome do produto mais barato é {nome_produto_barato}")