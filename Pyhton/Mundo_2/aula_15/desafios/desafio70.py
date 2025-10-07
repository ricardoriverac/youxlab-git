totalgasto = 0
produtosmil = 0
menor = 0
contador = 0
barato = ' '
while True:
    produto = str(input('Digite o nome do seu produto: '))
    preço = float(input('Digite o valor do seu produto: '))
    contador = contador + 1
    totalgasto = totalgasto + preço
    if preço > 1000:
        produtosmil = produtosmil + 1
    if contador  == 1:
        barato = produto
        menor = preço
    else:
        if preço < menor:
            menor = preço 
    continuando = ' '
    while not continuando in 'SN':
        continuando = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuando == 'N':
        break
print('Acabou!')
print(f'A compra ficou no total de R$ {totalgasto}')
print(f'Temos {produtosmil} produtos custando mais de mil reais')
print(f'O produto mais barato foi {barato} e custa R${menor}')