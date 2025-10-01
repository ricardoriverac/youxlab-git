total = maisDeMil = menor = contador = 0
barato = ''
while True:
    produto = str(input('informe um produto: '))
    preco = int(input('informe o preço desse produto: R$'))
    total += preco
    contador += 1
    if preco >= 1000:
        maisDeMil += 1
    if contador == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    confirmar = ' '
    while confirmar not in 'SN':
        confirmar = str(input('quer continuar?[S/N]')).strip().upper()[0]
    if confirmar == 'N':
            break
print(f'o total da compra foi R${total:.2f}')
print(f'{maisDeMil} produtos dentre todos os outros custam mais de mil reais')
print(f'{barato} é o produto mais barato e seu preço é R${menor:.2f}')