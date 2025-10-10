distancia = float(input('Qual a distancia da sua viagem?'))
print('Voce esta prestes a comecar uma viajem de {}km.')
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preco da sua viajem sera de {quilometros 0.50 } R${:.2f}'.format(preco))
