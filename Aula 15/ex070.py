total = totalmil = menor = contador = 0
barato = ' '
while True:
    produto = str(input('Nome do produto : '))
    preço = float(input('Preço do produto  :R$ '))
    contador += 1
    total += preço
    if preço > 1000:
        totalmil += 1
    if contador  == 1:
        barato = produto
        menor = preço
    else:
        if preço < menor:
            menor = preço 
    resposta = ' '
    while not resposta in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print('Acabou!')
print(f'A compra ficou no total de R$ {total : .2f}')
print(f'Temos {totalmil} produtos custando mais de mil reais')
print(f'O produto mais barato foi {barato} e custa R${menor : .2f}')