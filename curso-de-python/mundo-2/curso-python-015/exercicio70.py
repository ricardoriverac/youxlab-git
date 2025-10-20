resposta = "S"
cont = 0
soma = 0
quantidadeDeProdutosAcimaDe1000 = 0
while resposta == "S":
    nome = str(input('digite o nome do produto'))
    preço = float(input('valor do produto: R$'))
    if preço >1000:
        quantidadeDeProdutosAcimaDe1000 += 1
    if cont == 1:
        menor = preço
    









    resposta = str(input(f'voce deseja continua? [S/N]: ')).upper()