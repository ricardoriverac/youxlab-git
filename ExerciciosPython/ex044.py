print('{:=^40}'.format('LOJAS JUJU'))
precoNormal = float(input('Preço das compras:R$'))
print('''FORMAS DE PAGAMENTO
[1] á vista dinheiro/cheque
[2] á vista cartão
[3] 2x no cartão 
[4] 3x ou mais no cartão''')
opcoes = int(input('Qual é a opção: '))

if opcoes == 1:
        total = precoNormal - (precoNormal * 10 / 100)
elif opcoes == 2:
        total = precoNormal - (precoNormal * 5 / 100)
elif opcoes == 3:
        total = precoNormal 
        parcela = total / 2
        print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opcoes == 4:
        total = precoNormal + (precoNormal * 20 / 100)
        parcela = total / 3
        totalParcela = int(input('Quantas parcelas: '))
        parcela = total / totalParcela
        print(f'Sua compra será parcelada em {totalParcela}x de R${parcela:.2f} COM JUROS')
else:
    total = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print(f'Sua compra de R${precoNormal:.2f} vai custar R${total:.2f} no final.')
