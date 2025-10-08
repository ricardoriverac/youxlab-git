km = int(input('Qual a distancia da sua viagem em km: '))
if km < 200:
    valortotal = 0.50 * km
    print (f'O valor total da sua viagem è {valortotal}')
else:
    valortotal = 0.45 * km
    print(f'Sua viagem ultrapassou 200, o preço e de {valortotal}')