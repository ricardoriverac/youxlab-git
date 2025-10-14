import moeda

p = float(input('Preço: R$'))
t = int(input('Qual será a taxa sobre o preço? '))
print(f'O aumento de {t}%  em {moeda.real(p)} é {moeda.real(moeda.aumentar(p, t))}')
print(f'O desconto de {t}%  em {moeda.real(p)} é {moeda.real(moeda.diminuir(p, t))}')
print(f'O dobro de {moeda.real(p)} é {moeda.real(moeda.dobro(p))}')
print(f'A metade de {moeda.real(p)} é {moeda.real(moeda.metade(p))}')