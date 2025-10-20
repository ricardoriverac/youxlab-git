from d108 import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.real(preco)} é {moeda.real(moeda.metade(preco))}')
print(f'O dobro de {moeda.real(preco)} é {moeda.real(moeda.dobro(preco))}')
print(f'Com o aumento de 10% temos {moeda.real(moeda.aumentar(preco,10))}')