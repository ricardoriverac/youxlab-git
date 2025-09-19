velocidade = float(input('Em qual velocidade vc esta? '))
if velocidade > 80: 
    print('MULTADO, você ultrapassou o limite que é 80km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia!')
