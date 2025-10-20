from d109 import moeda 

preco = float(input('Digite o preço: R$'))
print(f'A metade de {preco} é {moeda.metade(preco, True)}')
print(f'O dobro de {preco} é {moeda.dobro(preco, True)}')
print(f'Com o aumento de 10% temos {moeda.aumentar(preco, 10, True)}')
print(f'Reduzindo 10% temos {moeda.diminuir(preco, 10, True)}')