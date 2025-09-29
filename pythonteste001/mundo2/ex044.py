print('{:=^60}'.format(' LOJAS JUBRISCREU '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque 
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela  = total / 2
    print('Sua compra será dividida em 2 parcelas de R${:.2f}.'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    parcelastotais = int(input('Dejesa parcelar em quantas vezes? '))
    parcelas = total / parcelastotais
    print('Sua compra será dividida em {} parcelas de R${:.2f}, COM JUROS.'.format(parcelastotais,parcelas))
else:
    print('\033[0;31;47mFORMA DE PAGAMENTO INVÁLIDA! TENTE NOVAMENTE!\033[m')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
confirmação = input('Tem certeza que deseja prosseguir com esta forma de pagamento? ')
# voltar depois para fazer um jeito de comfirmar o modo de pagamento
