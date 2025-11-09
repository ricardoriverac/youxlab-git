from python107 import moeda

preco = float(input('Digite o preço R$:'))
print(f'A metade de R${preco} é {moeda.metade(preco)}')
print(f'O dobro de R${preco} é R${moeda.dobro(preco)}')
print(f'Aumento 10%, temos R${moeda.aumentar(preco, 10)}')
