from uteis import moeda

p = int(input('Digite o preço: R$ '))
print(f'A metade de {p} é R${moeda.monetario(round(moeda.metade(p)))}')
print(f'O dobro de {p} é R${moeda.monetario(round(moeda.dobro(p)))}')
print(f'Aumentando 10%, temos R${moeda.monetario(round(moeda.aumentar(p)))}')
print(f'Reduzindo 13%, temos R${moeda.monetario(round(moeda.diminuir(p)))}')
print(f'R${moeda.monetario(round(moeda.diminuir(p)))}')
