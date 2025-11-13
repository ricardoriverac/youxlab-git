import moeda

preco = float(input('Digite o preço R$: '))
print(f'A metade de {moeda.reais(preco)} é {moeda.reais(moeda.metade(preco))}')
print(f'O dobro de {moeda.reais(preco)} é {moeda.reais(moeda.dobro(preco))}')
print(f'Aumentando 10%, temos {moeda.reais(moeda.aumentar(preco, 10))}')