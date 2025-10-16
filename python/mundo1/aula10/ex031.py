#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
# parta viagens mais longas.

distan = float(input('Qual a distância da sua viagem em km: '))
calculo = distan * 0.50
if distan <= 200:
    print(f'O valor a pagar é de R${calculo} por km percorrido.')
else:
    calcu = distan * 0.45
    print(f'O valor a pagar de acordo com o km percorrido a mais de 200km é de R${calcu}')


