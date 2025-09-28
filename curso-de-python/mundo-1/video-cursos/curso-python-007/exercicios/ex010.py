real = float(input('Quantos dinheiro você tem na carteira? R$'))
dolar = real / 5.45
print('Com R${:.2f} pode-se comprar US${:.2f}'.format(real, dolar))