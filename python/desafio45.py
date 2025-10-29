print('=== Loja do Wendel ===')
preco = float(input('Preço das compras: R$ '))
print('''Formas de pagamento:
[ 1 ] à vista em dinheiro ou cheque
[ 2 ] à vista no cartão (5% de desconto)
[ 3 ] em até 2x no cartão (preço normal)
[ 4 ] 3x ou mais no cartão (20% de juros)''')
opcao = int(input('Escolha a opção de pagamento: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print(f'Pagamento à vista em dinheiro/cheque. Desconto de 10%.')
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print(f'Pagamento à vista no cartão. Desconto de 5%.')
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Compra parcelada em 2x de R${parcela:.2f} SEM juros.')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    valor_parcela = total / parcelas
    print(f'Compra parcelada em {parcelas}x de R${valor_parcela:.2f} COM juros.')
else:
    total = preco
    print('Opção inválida. Tente novamente.')
print(f'Total a pagar: R${total:.2f}')
