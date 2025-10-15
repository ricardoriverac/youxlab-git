import teste
num = float(input('Digite o preço: R$'))
des = int(input('Digite o aumento/desconto: '))
print('-'*30, f'\nPreço: {teste.moeda(num)}\nAumento: {teste.aumentar(num, des, True)}')
print('-'*30, f'\nPreço: {teste.moeda(num)}\nDesconto: {teste.diminuir(num, des, True)}')
print('-'*30, f'\nPreço: {teste.moeda(num)}\nDobro: {teste.dobro(num, True)}')
print('-'*30, f'\nPreço: {teste.moeda(num)}\nMetade: {teste.metade(num, True)}')