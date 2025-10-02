precocompras = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão 
[4] 3x ou mais vezes no cartão''')
pagamento = int(input('Qual é a sua opção:'))
parcelas = int(input('Quantas parcelas?:'))
if pagamento == 1:
 total = precocompras - (precocompras * 10/ 100)

elif pagamento == 2:
  total = precocompras - (precocompras * 5/ 100)

elif pagamento == 3:
  total = precocompras
  parcelas = total / 2
elif pagamento == 4:
  total = precocompras + (precocompras * 0.2 )
  print('Sua compra será parcelada em {}x de R${} com juros'.format(parcelas,total))
  print('Sua compra de R${} vai custar R${} no final'.format(precocompras,total))
