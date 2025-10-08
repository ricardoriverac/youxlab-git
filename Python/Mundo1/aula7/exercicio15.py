dias = int(input('Quantos dias alugados : '))
km = float(input('Quantos km percorrido: '))
pago = (dias * 60) + (km * 0.15) 
print ('O total a ser pago e de R${:.2f}'.format(pago))