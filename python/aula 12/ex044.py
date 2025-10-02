valor = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('qual é a opção? '))
desconto = valor - (valor * 10 / 100)
if opcao == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, desconto))
elif opcao == 2:
    desconto = valor - (valor * 5 / 100)
    print('Sua compra de R$ {:.2f} vai custar {:.2f} no final'.format(valor, desconto))
elif opcao == 3:
    prestacao = valor / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS'.format(prestacao))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = valor + (valor * 20 / 100)
    prestacao = juros / parcelas
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(parcelas, prestacao))
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(valor, juros))
else:
    print('Opçao invalida tente alguma informada a cima')