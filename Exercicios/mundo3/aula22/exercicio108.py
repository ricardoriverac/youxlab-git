import _moeda

preco = float(input("Digite o preço: R$ "))

print(f"A metade de {_moeda(preco)} é {_moeda.metade(preco, True)}")
print(f"O dobro de {_moeda.moeda(preco)} é {_moeda.dobro(preco, True)}")
print(f"Aumentando 10%, temos {_moeda.aumentar(preco, 10, True)}")
print(f"Diminuindo 13%, temos {_moeda.diminuir(preco, 13, True)}")