velocidade = float(input('qual é a velocidade do carro?'))
if velocidade > 80:
    print ('multado! voce excedeu o limite permitido que é 80 KM/h')
    multa = (velocidade-80) * 7
    print(f'voce deve pagar uma multa de R${multa}')
