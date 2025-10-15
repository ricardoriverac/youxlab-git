import teste
num = float(input('Digite o preço: R$'))
des = int(input('Digite o aumento/desconto: '))
print('-'*30, f'\nPreço: {teste.moeda(num)}\nAumento: {teste.moeda(teste.aumentar(num))}')
print('-'*30, f'\nPreço: {teste.moeda(num)}\nDesconto: {teste.moeda(teste.diminuir(num))}')
print('-'*30, f'\nPreço: {teste.moeda(num)}\nDobro: {teste.moeda(teste.dobro(num))}')
print('-'*30, f'\nPreço: {teste.moeda(num)}\nMetade: {teste.moeda(teste.metade(num))}')