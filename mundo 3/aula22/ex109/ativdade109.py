import moeda109

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda109.moeda(p)} é {moeda109.metade(p, True)}')