preco = float(input('preco das compras: R$'))
print('''formas de pagamento)
[1] a visita dinheiro
[2] a vista cartao
[3] 2x no cartao
[4] 3x ou mais no cartao''')
opcao = input(input('qual a opcao?'))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    parcela = total / 2

    print('sua compra sera parcelada em 2x de R${:.2f}'.format(parcela))
print('sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))



