from python.mundo3.aula22.uteis.utilidadesCev import moeda

p = int(input('Digite o preço: R$ '))
print(f'A metade de {moeda.monetario(p)} é {moeda.metade(p, False)}')
print(f'O dobro de {moeda.monetario(p)} é {moeda.dobro(p, False)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, True)}')
print(f'Reduzindo 13%, temos R${moeda.diminuir(p, True)}')
print(f'R${moeda.diminuir(p, True)}')