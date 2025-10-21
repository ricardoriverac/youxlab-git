precoDproduto = float(input('Digite o valor do produto :'))

print("""Qual opcao voce vai escolher
      [1] A VISTA dinheiro/cheque
      [2] A VISTA cartao
      [3] 2x no cartao
      [4] 3x ou mais no cartao:20% juros""")
opcao = str(input('Qual opcao voce vai escoher? '))
if opcao == '1':
    pagar = precoDproduto * 0.10
    print(f'O total a pagar sera de {pagar}')
elif opcao == '2':
    pagar2 = precoDproduto * 0.5
    print(f'O valor a pagar sera de {pagar2}')
elif opcao == '3':
    pagar3 = precoDproduto /2
    print(f'O valor a pagar sera de {pagar3}')
elif opcao == '4':
    pagar4 = precoDproduto * 1.20
    print(f'O valor a pagar sera de {pagar4}')
