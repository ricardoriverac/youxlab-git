#algoritmo que lê o preço de um produto e mostra seu novo preço com 5% de seu desconto

prod = float(input('Escaneie o preço: '))
print('O preço final do produto é {}'.format(prod - (prod*(5/100))))