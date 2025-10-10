import _moeda 

i = float(input("Digite o preço: R$ "))
print(f"A metade de {i} é {_moeda.metade(i)}")
print(f"O dobro de {i} é {_moeda.dobro(i)}")
print(f"Aumentando 10% de {i}, temos {_moeda.aumentar(i, 10):.2f}")
print(f"Diminuindo 10% de {i}, temos {_moeda.diminuir(i, 10):.2f}")