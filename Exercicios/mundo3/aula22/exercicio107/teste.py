import moeda

numero = float(input("Digite o preço: R$ "))
print(f"A metade de {numero} é {moeda.metade(numero)}")
print(f"O dobro de {numero} é {moeda.dobro(numero)}")
print(f"Aumentando 10% de {numero}, temos {moeda.aumentar(numero, 10):.2f}")
print(f"Diminuindo 10% de {numero}, temos {moeda.diminuir(numero, 10):.2f}")