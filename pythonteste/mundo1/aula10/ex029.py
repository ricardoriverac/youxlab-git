velocidade=float(input('qual a velocidade atual do seu carro? '))
if velocidade>80:
    print('MULTADO! você excedeu o limite de velocidade permitido de 80Km/h')
    multa=(velocidade-80)*7
    print('voce deve pagaruma multa de R${:.2f}!'.format(multa))
print('tenha um bom dia! diriga com segurança!')
