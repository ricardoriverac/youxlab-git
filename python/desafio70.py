total = mais1000 = menor_preco = 0
produto_barato = ''

print('-' * 30)
print('      LOJA SUPER BARATÃO')
print('-' * 30)

while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    total += preco

    if preco > 1000:
        mais1000 += 1

    if menor_preco == 0 or preco < menor_preco:
        menor_preco = preco
        produto_barato = nome

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-' * 30)
print(f'Total gasto na compra: R${total:.2f}')
print(f'Temos {mais1000} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {produto_barato} que custa R${menor_preco:.2f}')
print('-' * 30)
