
import moeda

numero = float(input("Digite o preço: R$ "))

print(f"A metade de {moeda.moeda(numero)} é {moeda.metade(numero)}")
print(f"O dobro de {moeda.moeda(numero)} é {moeda.dobro(numero)}")
print(f"Aumentando 10% de {numero}, temos {moeda.moeda(moeda.aumentar(numero, 10))}")
print(f"Diminuindo 10% de {numero}, temos {moeda.moeda(moeda.diminuir(numero, 10))}")