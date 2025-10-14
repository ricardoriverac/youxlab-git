from utilidadescev import dado
from utilidadescev import moeda

dobro = metade = 0
valor = dado.leiadinheiro(int(input('Digite um  valor:')))
print('-=' * 15)
print(' ANALISANDO O VALOR')
print('-=' * 15)
print(f'Preco analisado {valor}')
print(f'Dobro do preco {moeda.dobro(valor)}')
print(f'Metade do preco {moeda.metade(valor)}')
print(f'Com aumento de 35% {moeda.aumentar(valor+35)}')
print(f'Com a reducao de 22% {moeda.diminuir(valor-22)}')
print('-=' *15)