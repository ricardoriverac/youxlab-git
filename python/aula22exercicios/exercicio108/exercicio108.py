import formatacao108
num = float(input('Digite o preço: R$'))
des = int(input('Digite o aumento/desconto: '))
print('-'*30, f'\nPreço: {formatacao108.moeda(num)}\nAumento: {formatacao108.moeda(formatacao108.aumentar(num))}')
print('-'*30, f'\nPreço: {formatacao108.moeda(num)}\nDesconto: {formatacao108.moeda(formatacao108.diminuir(num))}')
print('-'*30, f'\nPreço: {formatacao108.moeda(num)}\nDobro: {formatacao108.moeda(formatacao108.dobro(num))}')
print('-'*30, f'\nPreço: {formatacao108.moeda(num)}\nMetade: {formatacao108.moeda(formatacao108.metade(num))}')
