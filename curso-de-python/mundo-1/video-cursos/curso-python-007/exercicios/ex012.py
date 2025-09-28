preco = float(input('Diga o valor do produto: '))
novo = preco - (preco * 5 / 100)
print('O valor deste produto é {:.2f}, com a promoção de 5% de desconto fica por {:.2f}'.format(preco, novo))