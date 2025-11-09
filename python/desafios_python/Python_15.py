aluguel = float(input('Quantos dias alugados?:'))
km = float(input('Quantos Km rodados?:'))
calculo = (aluguel * 60) + (km * 0.15)
print(f'O total a pagar é de R${calculo:.2f}')

