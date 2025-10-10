real = float(input('quantos reais você tem? R$'))
dolar = real / 5.46
euro = real / 6.36
iene = real * 27.14
print('com R${:.2f}, você pode comprar {:.2f} dólares, {:.2f} euros e {:.2f} ienes'.format(real, dolar, euro, iene))