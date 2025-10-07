print('LOJA DO SUPER BARATÃO! ')
continuação= 'a'
barato= ''
valorFinal=0
countValor=0
maisBarato=100000000
while continuação not in 'N':
    Produto= str(input('Qual o nome do produto?'))
    valor= float(input('Qual o valor do produto? '))
    if valor > 1000:
        countValor+=1
    elif maisBarato>valor:
        maisBarato=valor
        barato=Produto
    valorFinal=valor+valorFinal
    continuação= str(input('Você quer continuar a compra? [S/N] ')).upper()
print(f'O total da compra foi {valorFinal}R$')
print(f'Temos {countValor} produtos custando mais de 1000 R$')
print(f'O produto mais barato foi {barato} custando {maisBarato:.2f} R$')
