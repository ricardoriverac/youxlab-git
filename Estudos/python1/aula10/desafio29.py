tempo=float(input('Quanto tempo durou sua viagem dentro do carro? [horas]'))
distancia= float(input('Qual foi a distancia percorrida? [km/h]'))
velocidade = distancia/tempo
if velocidade >=80:
    velocidadeExtra= (velocidade - 80)
    multa= velocidadeExtra * 7.00
    print(f'Você foi multado em {multa}!!')
else:
    print('Você está na velocidade adequada!')