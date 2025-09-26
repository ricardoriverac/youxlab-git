km = float(input('Qual é a distância da sua viagem? '))
print(f'Você esta prestes a começar uma viagem de {km}km.')
passagem = 0.50*km
if km <= 200:
    print(f'O preço da sua passagem será de R${passagem} ')
else:
    passagem2 = 0.45*km
    print(f'O preço da sua passagem será de R${passagem2}')