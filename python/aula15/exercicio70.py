total = qntdMilio = count = maior = menor = 0
menorNome = ' '
while True:
    print('-'*20, '\nLOJA SUPER BARATÃO\n', '-'*20)
    nomeDoProduto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    count += 1
    if preco >= 1000:
        qntdMilio += 1
    total += preco  
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
    if count == 1:
        maior = menor = preco
        menorNome = nomeDoProduto
    if preco > maior:
        maior = preco
    elif preco < menor:
        menor = preco
        menorNome = nomeDoProduto
        
print(f'''{total}
{qntdMilio}
{menorNome}''')
    
    