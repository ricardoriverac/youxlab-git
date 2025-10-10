total = = 0 
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    total += preço 
    if preço > 1000:
        totmil += 1

    resp = ''
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-40}'.format(' Fim do programa'))
print(f'O total de compra foi R${total:.2f}')