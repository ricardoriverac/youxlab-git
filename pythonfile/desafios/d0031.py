viagem = float(input('Qual a distancia da sua viagem em km/h? '))
preco_da_viagem = viagem *0.50
preco_da_viagem_mais200 = viagem *0.45
if viagem <200:
    print(f'O preço da sua viagem é {preco_da_viagem}')
else:
    print(f'O preço da sua viagem é {preco_da_viagem_mais200}')