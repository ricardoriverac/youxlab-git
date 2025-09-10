velocidade = float(input('qual a velocidade do seu corsa?'))
if velocidade>80:
    print('carai esse corsa ta turbinado!')
    multa = velocidade *7
    print(' EU AVISEI MANO,TOMOU A MULTA DE DE R${:.2f}!'.format(multa))
else:
    print('ai sim,ta andando com segurança e sem risco de tomar uma multa')