distancia= float(input('Qual a distancia da corrida? [km] '))
if distancia > 200:
    print(f'O valor da corrida é {distancia * 0.45} ')
else:
    print(f'O valor da corrida é {distancia * 0.50}')