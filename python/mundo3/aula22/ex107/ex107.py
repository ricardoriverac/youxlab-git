#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
# dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.


import moeda
preco = float(input('Digite o valor da sua compra:R$'))
print(f'A metade de R${preco} é:R${moeda.metade(preco)}')
print(f'O dobro de R${preco} é:R${moeda.dobro(preco)}')
print(f'O valor da compra com o aumento de 10% é:R${moeda.aumento(preco)}')
print(f'O valor da compra com o reduzimento de 13% é:R${moeda.diminuir(preco)}')
