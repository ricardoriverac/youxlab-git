from desafio109 import moeda

preco = float(input('Digite um preço :'))
print(f"A metade de {moeda.moeda(valor)} é {moeda.metade(preco), True}")
print(f"O dobro de {moeda.moeda(valor)} é {moeda.dobro(preco, True)}")
print(f"Mais 10% de {moeda.moeda(valor)} é {moeda.aumentar(preco, 10, True)}")
print(f"Menos 10% de {moeda.moeda(valor)} é {moeda.diminuir(preco, 10, True)}")

# nao entendi