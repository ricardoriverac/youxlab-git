# from exercicio108 import moeda
# Preço = float(input('digite o preço: R$'))



from exercicio108 import moeda

preço = float(input("Digite o preço: R$ "))
print(f"A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}")
print(f"O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro)}")
print(f"Aumentando 10%, temos {moeda.aumentar(preço, 10, True)}")
print(f"Diminuindo 13%, temos {moeda.diminuir(preço, 13, True)}")