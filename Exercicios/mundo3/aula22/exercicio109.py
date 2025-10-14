import _moeda

i = float(input('Digite o preço: R$ '))
print(f'O dobro de {_moeda.moeda(i)} é {_moeda.dobro(i, True)}')
print(f'A metade de {_moeda.moeda(i)} é {_moeda.metade(i, True)}')
print(f'Aumentando 10% de {i}, {_moeda.aumentar(i, 10, True)}')
print(f'Aumentando 10% de {i}, {_moeda.diminuir(i, 10, True)}')