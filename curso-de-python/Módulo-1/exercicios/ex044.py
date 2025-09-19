produto = float(input('Digite o valor do produto: '))
escolhaPagamento = str(input('Escolha o método de pagamento: \nDinheiro\nCheque\nA Vista\n2x no Cartão\n3x ou mais\n\n-->  ')).replace('cartao', 'cartão').lower()
if escolhaPagamento == 'dinheiro' or escolhaPagamento == 'cheque' or escolhaPagamento == '2x no cartão':
    print(f'Em Dinheiro ou Cheque, você recebe 10% de desconto! O valor do produto ficou em R${produto - (produto * 10 / 100) :.2f}')
elif escolhaPagamento == 'a vista':
    print(f'A vista no cartão você recebe 5% de desconto! O valor do produto ficou em R${produto - (produto * 5 / 100) :.2f}')
elif escolhaPagamento == '2x no cartão':
    print(f'Em 2x no cartão o preço do produto continua o mesmo.')
elif escolhaPagamento == '3x ou mais':
    print(f'Em 3x ou mais, terá 20% de juros! O preço do produto ficou em R${produto + (produto * 20 / 100) :.2f}')