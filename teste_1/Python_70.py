total = totalmil = menor = conta = 0
barato = '' 

print('-=' * 30)
print('LOJA SUPER BARATÃO')
print('-=' * 30)
while True:

    produto = str(input('Nome do produto: '))
    preco = int(input('Preço: R$'))
    conta += 1
    total += preco

    if preco > 1000:
        totalmil += 1

    if conta == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ''

    resp = input('Quer continuar? [S/N]: ').strip().upper()

    if resp == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totalmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
