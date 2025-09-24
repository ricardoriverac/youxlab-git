preco = int(input('Digite o preço das compras: R$'))
forma_pagamento = int(input('''Formas de pagamento: 
[1] á vista Dinheiro
[2] á vista no cartão de crédito
[3] 2x no cartão de crédito
[4] 3x ou mais no cartão de crédito'''))
escolha = int(input('Escolha a forma de pagamento: '))
if escolha==1:
    total = preco - (preco * 10 / 100)
    print(f'Sua compra vai custar R${total} no final')
elif escolha == 2:
    total = preco - (preco * 5 / 100)
    print(f'Sua compra vai custar R${total} no final')
elif escolha == 3:
    total = preco
    parcelas = total / 2
    print(f'Sua compra vai custar R${total} no final')
elif escolha == 4:
    total = preco + (preco * 20 / 100)
    totaldparcela = int(input('Em quantas parcelas? '))
    parcela = total / totaldparcela
    print(f'Sua compra será parcelada em {totaldparcela}x de R${parcela} com juros')