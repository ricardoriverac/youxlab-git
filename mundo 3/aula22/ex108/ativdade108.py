import moeda108 

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda108.moeda(preco)} é {moeda108.moeda(moeda108.metade(preco))}')