import moeda

p = float(input('Preço: R$'))
t = int(input('Qual será a taxa sobre o preço? '))
print(f'O aumento de {t}% em {moeda.moeda(p)} é {moeda.aumentar(p, t, True)}')
print(f'O desconto de {t}% em {moeda.moeda(p)} é {moeda.diminuir(p, t, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
