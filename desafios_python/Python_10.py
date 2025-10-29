real = float(input('Quanto dinheiro você tem na carteira? R$:'))
dolar = real / 5.31
print (f'Com R${real:.2f} você pode comprar US${dolar:.2f} dólares')
euro = real / 6.28
print (f'Com R${real:.2f} você pode comprar C${euro:.2f} euros')