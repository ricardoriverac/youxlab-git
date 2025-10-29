dias = int(input('quantos dias alugados?'))
km = float(input('Quantos km rodado?'))
pago = (dias * 60 ) + (km * 0.15)
print(f'O total a ser pagado será R${pago}')