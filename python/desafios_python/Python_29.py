velocidade1 = float(input('Qual é a velocidade atual do carro?:'))
if velocidade1 > 80:
    print('MULTADO! Você ultrapassou o limite permitido que é de 80km/h')
    multa = (velocidade1-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!' .format(multa))
    print('Tenha um bom dia! Dirija com segurança')
else:
    print(('Parabén você está dentro do limite de velocidade! Continue asssim :)'))