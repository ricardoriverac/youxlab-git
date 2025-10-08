'''
Exercício Python 015: Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de dias pelos quais ele foi
alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por
dia e R$0,15 por Km rodado.
'''

carro_dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
carro_km = float(input('Digite a quantidade de km percorrido pelo carro: '))
total = carro_dias * 60 + carro_km * 0.15
print(f'A quantidade a pagar somando o km percorrido e o dia alugado foi de: {total}')

