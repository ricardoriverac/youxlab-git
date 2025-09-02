#Converte o saldo em reais para dólares
quantidadeEmReais = float (input ('Insira seu saldo'))
quantidadeDeDolares = round((quantidadeEmReais / 3.27), 2)
print ('{} reais são convertidos em {} dólares'.format(quantidadeEmReais,quantidadeDeDolares))