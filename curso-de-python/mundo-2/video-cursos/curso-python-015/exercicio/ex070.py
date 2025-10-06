nome = 0
preco = 0
soma = 0
count = 0
produtoMil = 0
menorPreco = 0
nomeMenorPreco = ''

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    soma += preco
    count += 1

    if count == 1:
        menorPreco = preco
        nomeMenorPreco = nome
    else:
        if preco < menorPreco:
            menorPreco = preco
            nomeMenorPreco = nome

    if preco > 1000:
        produtoMil += 1

    continuar = str(input('Você deseja adicionar mais produtos? [S/N]  ')).upper()
    if continuar == 'N':
        break

print(f'O valor total gasto na compra é de R${soma}')
print(f'{produtoMil} produtos custam mais que R$1000.')
print(f'O nome do produto mais barato é {nomeMenorPreco} que custa R${menorPreco:.2f}')