from desafio107 import moeda

preco = float(input('Digite um valor:'))
print(f'A metade de R${moeda.real(preco)} é {moeda.real(moeda.metade(preco))}')
print(f'O dobro de {moeda.real(preco)} é {moeda.real(moeda.dobro(preco))}')
print(f'Aumentando 10%, temos {moeda.real(moeda.aumentar(preco+10))}')

#nao entendi