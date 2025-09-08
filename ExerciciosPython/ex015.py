dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos km rodados?'))
carro = 60.00
tempo = dias*carro
distancia = 0.15*km
resto = tempo+distancia
print(f'O total a pagar é de R${resto:.2f}')