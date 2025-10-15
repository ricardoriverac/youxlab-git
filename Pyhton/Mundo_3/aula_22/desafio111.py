import moeda
preco = str(input('Digite o preço: R$ '))
pr = preco.replace(',', '.')  # troca ',' por '.'
# moeda.resumo(float(pr), 80, 35)
moeda.resumo(float(pr))