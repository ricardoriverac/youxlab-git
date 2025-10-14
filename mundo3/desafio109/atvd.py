import moeda
p = float(input('Preço: R$'))
t = int(input('Qual será a taxa sobre o preço? '))
print(f'O aumento de {t}%  em {moeda.real(p)} é {moeda.aumentar(p, t, True)}')
print(f'O desconto de {t}%  em {moeda.real(p)} é {moeda.diminuir(p, t, True)}')
print(f'O dobro de {moeda.real(p)} é {moeda.dobro(p, True)}')
print(f'A metade de {moeda.real(p)} é {moeda.metade(p, True)}')