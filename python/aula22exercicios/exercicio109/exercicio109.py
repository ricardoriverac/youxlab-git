import formatacao109
num = float(input('Digite o preço: R$'))
des = int(input('Digite o aumento/desconto: '))
print('-'*30, f'\nPreço: {formatacao109.moeda(num)}\nAumento: {formatacao109.aumentar(num, des, True)}')
print('-'*30, f'\nPreço: {formatacao109.moeda(num)}\nDesconto: {formatacao109.diminuir(num, des, True)}')
print('-'*30, f'\nPreço: {formatacao109.moeda(num)}\nDobro: {formatacao109.dobro(num, True)}')
print('-'*30, f'\nPreço: {formatacao109.moeda(num)}\nMetade: {formatacao109.metade(num, True)}')
