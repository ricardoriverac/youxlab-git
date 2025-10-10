import moeda

p = float(input('Preço: R$'))
t = int(input('Qual será a taxa sobre o preço? '))
print(f'O aumento de {t}% em {p} é {moeda.aumentar(p, t)}')
print(f'O desconto de {t}% em {p} é {moeda.diminuir(p, t)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'A metade de {p} é {moeda.metade(p)}')