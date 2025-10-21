distancia = int(input('Digite a distancia da viagem em: '))
if distancia <= 200:
    preco = distancia *0.50
    print(f'O preço da passagem sera de R$ {preco}')
else:
    preco2 = distancia *0.45
    print(f'O preço da passagem sera de R$ {preco2}')

