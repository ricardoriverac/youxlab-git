resposta = 's'
totalGasto = 0
somaProdutos = 0
valorProdutoBarato = 99999999
nomeProdutoBarato = ''
produtosMais1000 = 0
while resposta == 's':
    nomeProdutos = str(input('Nome do produto: '))
    precoProdutos = float(input('Valor do produto: R$'))
    somaProdutos += precoProdutos
    if precoProdutos >= 1000:
        produtosMais1000 += 1
    if precoProdutos < valorProdutoBarato:
        valorProdutoBarato = precoProdutos
        nomeProdutoBarato = nomeProdutos
        resposta = str(input('Você deseja continuar? [s/n]: '))
print(f'O valor gasto na compra foi de R${somaProdutos}.\nQuantidade de produtos mais de R$1000: {produtosMais1000}.\nO nome do produto mais barato é: {nomeProdutoBarato} e o teu valor é de: {valorProdutoBarato}.')