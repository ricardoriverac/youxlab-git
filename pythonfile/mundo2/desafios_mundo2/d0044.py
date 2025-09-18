#Entradas
preco = float(input('Digite um preço'))
condicao = str(input('Digite a forma de pagamento'))
if condicao == 'cartão' :

    parcela = int(input('Digite como quer parcelar'))
desconto = -1
valor_final = -1

#Cálculo/Processamento
if condicao == 'dinhero' or condicao == 'cheque' :
    desconto = 0.1
elif condicao == 'cartão' and parcela == 1:
    desconto = 0.05
elif condicao == 'cartão' and parcela == 2:
    desconto = 0
elif condicao == 'cartão' and parcela >=3:
    desconto = -0.2

#Saída
valor_final = preco - ( desconto *preco )
print(f'O Valor final será: {valor_final}')