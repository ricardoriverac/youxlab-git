continuar = 's'
soma = 0
produtocontador1000 = 0
produtoMenorPrecoPreco = 9999999990
produtoMenorPrecoNome = ''
while continuar == 's':
    produtoNome = str(input('Digite o nome do seu produto: '))
    produtoPreco =  float(input('Preço do seu produto: R$ '))
    continuar = str(input('Quer continuar? [S/N]: ')).lower()[0]
    soma += produtoPreco
    if produtoPreco >= 1000:
        produtocontador1000 += 1
    if produtoPreco < produtoMenorPrecoPreco:
        produtoMenorPrecoNome = produtoNome
        produtoMenorPrecoPreco = produtoPreco



print(f'O total gasto foi de R${soma} reais.')
print(f'Produtos {produtocontador1000} custam mais de 1000')
print(f'O o produto mais barato é o {produtoMenorPrecoNome} e seu preço é R${produtoMenorPrecoPreco:.2f} reais.')