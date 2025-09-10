velocidade = int(input('Quantos km seu carro estava? '))
multa = (velocidade - 80) * 7
if velocidade>80:
    print('Seu carro foi multado!')
    print(f'Você precisa pagar a multa de R${multa}')
else:
    print('O limite de velocidade é 80km e sua velocidade é {}'.format(velocidade))
    print('Você está dentro do limite de velocidade! ')