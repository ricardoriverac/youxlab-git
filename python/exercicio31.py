distancia = float(input('Qual a distancia da viagem? '))
if distancia < 200:
    distan_pequena = distancia * 0.50
    print ('o valor da sua viagem sera {}R$, pois é uma viagem curta'.format(distan_pequena))
else:
    distan_longa = distancia * 0.45
    print ('O valor da sua viagem sera {}, pois é uma viagem longa'.format(distan_longa))
