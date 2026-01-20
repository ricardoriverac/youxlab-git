'''
Elabore um programa que calcule o valor a ser pago por um produto.
considerando o seu preço normal a condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preso normal
- 3x ou mais no cartão: 20% de juros
'''

#Resposta

preco_compra = float(input('Digite o valor das compras: '))
print('''
    FORMA DE PAGAMENTO
-=-=-=-=-=-=-=-=-=-=-=-=-=
    
[ 1 ] - à vista dinheiro/cheque: 10% de desconto
[ 2 ] - à vista no cartão: 5% de desconto
[ 3 ] - em até 2x no cartão: preso normal
[ 4 ] - 3x ou mais no cartão: 20% de juros
      
digite qual a forma que deseja pagar!!
''')

forma_do_pagamento = int(input('Digte a opição da forma de pagamento: '))
opicao1 = (preco_compra * 10) / 100
opicao2 = (preco_compra * 5) / 100
opicao4 = (preco_compra * 20) / 100
if forma_do_pagamento == 1 :
    calculo = preco_compra - opicao1
    print(f'\nO valor da compra é: {calculo}')

elif forma_do_pagamento == 2 :
    calculo2 = preco_compra - opicao2
    print(f'\nO valor da compra é: {calculo2}')

elif forma_do_pagamento == 3:
    print(f'\nO preço da compra e de {preco_compra}R$')

elif forma_do_pagamento == 4 :
    calculo3 = preco_compra + opicao4
    print(f'\nO valor da compra e equivalente a {calculo3}')