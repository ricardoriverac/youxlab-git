quilometros = int(input('Quantos quilometros tera sua viagem? '))
if quilometros <= 200:
    print(f'O preço da passagem dentro de 200Km será de R${quilometros * 0.50 :.2f}')
else:
    print(f'O preço da passagem acima de 200Km será de R${quilometros * 0.45 :.2f}')