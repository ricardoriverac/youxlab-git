preco = float(input('Digite o preço do produto: '))
print ('''FORMAS DE PAGAMENTO
[ 1 ] Á vista dinheiro/cheque
[ 2 ] A vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = input(input('Qual é a opção? '))
if opção == 1:
    total = preco - (preco * 10 / 100)
elif opção == 2:
    total = preco - (preco * 5 / 100)
elif opção == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra sera parcelada em 2x de R%${parcela}')
elif opção == 4:
    total = preco + (preco * 20 / 100)
    totparc = int (input('Quantas parcelas '))
    parcela = total / totparc
    print (f'Sua compra será parcelada em {totparc}x  de R${parcela} COM JUROS')
print(f'Sua compra de R${preco} vai custar R${total} no final')