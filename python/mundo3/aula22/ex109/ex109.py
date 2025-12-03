#Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

import moeda
p = float(input('Digite o valor da sua compra:R$'))
print(f'A metade de {moeda.moeda(p)} é:{moeda.metade(p, formatar=True)}')
print(f'O dobro de {moeda.moeda(p)} é:{moeda.dobro(p, True)}')
print(f'O valor da compra com 10% de aumento é:R${moeda.aumentar(p, True)}')
print(f'O valor da compra com o reduzimento de 13% é:R${moeda.diminuir(p, True)}')



