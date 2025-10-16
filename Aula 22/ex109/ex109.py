import moeda

i = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(i)} é {moeda.metade(i, True)}')
print(f'0 dobro de {moeda.moeda(i)} é {moeda.dobro(i, True)}')
print(f'Aumentande 10%, te {moeda.aumentar(i, 10, True)}')
print(f'Reduzinde 13%, temos {moeda.diminuir(i, 13, True)}')