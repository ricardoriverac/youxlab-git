#Exibe o preço do produto com 5% de desconto
precoDoProduto = float(input('Insira o preço do produto desejado '))
precoComDesconto = round(precoDoProduto - (precoDoProduto / 20))
print (f'O preço final do produto que vale {precoDoProduto:.2f} reais com desconto é de {precoComDesconto} reais')