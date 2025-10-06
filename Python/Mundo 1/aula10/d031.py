viagem = int(input('Qual a distancia da sua viagem? '))
valor = 0.50
valor2 = 0.45
if viagem >200:
    print('Vocẽ pagará: ' + str(viagem * valor))
else:
    print('Você pagará: ' + str(viagem * valor2))

