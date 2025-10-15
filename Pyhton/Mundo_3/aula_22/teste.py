from moeda import metade,dobro,aumentar

preco = float(input('Digite o preço: R$'))
print(f'A metade de R${preco} é R${moeda.metade(preco)}')
print(f'O dobro de R${preco} é R${moeda.dobro(preco)}')
print(f'Com o aumento de 10% temos R${moeda.aumentar(preco,10)}')