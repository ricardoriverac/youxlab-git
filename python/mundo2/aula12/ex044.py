#Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros

preco = float(input('Digite qual foi o preço da sua compra: R$ '))
print('1-Dinheiro/Cheque: ')
print('2-Cartão: ')
print('3-2x no cartão: ')
print('4-3x ou mais no cartão: ')
sugestao = int(input('Escolha uma das opçoẽs acima como forma de pagamento: '))
if sugestao == 1:
    soma = preco - (preco * 10 / 100)
    print(f'Sua compra com 10% de desconta vai custar R${soma}')
elif sugestao == 2:
    soma = preco - (preco * 5 / 100)
    print(f'Sua compra com o desconto de 5% vai custar R${soma}')
elif sugestao == 3:
    soma = preco
    parcela = preco / 2
    print(f'O valor da sua compra vai ser {soma}')
    print(f'Sua compra parcelada em 2x vai custar R${parcela}')
elif sugestao == 4:
    soma = preco + (preco * 20 / 100 )
    print(f'Sua compra vai sair no valor de R${soma}')