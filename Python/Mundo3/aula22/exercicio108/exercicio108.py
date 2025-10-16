
import moeda

valor = float(input("Digite o preço: R$ "))

print(f"A metade de {moeda.moeda(valor)} é {moeda.metade(valor)}")
print(f"O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor)}")
print(f"Aumentando 10% de {valor}, temos {moeda.moeda(moeda.aumentar(valor, 10))}")
print(f"Diminuindo 10% de {valor}, temos {moeda.moeda(moeda.diminuir(valor, 10))}")