from math import sqrt
velocidade = float(input('Velocidade do carro: '))
if velocidade >80:
    km = (velocidade - 80) * 7
    print('você foi MULTADO em R${:.2f}!'.format(km))
else:
    print('Velocidade PERMITIDA, Boa Viagem!')