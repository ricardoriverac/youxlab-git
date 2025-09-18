valorPago = float(input('Digite o valor: '))
print('''EScola a opção de pagamento:
      [ 1 ] à vista (dinheiro)
      [ 2 ] à vista (cartão) -> 5% de desconto
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão -> 20% de juros''')
opcao = int(input('Digite a opção: '))
if opcao == 1:
    print(f'O valor a ser pago será de {valorPago * 10/100}')
elif opcao == 2:
    print(f'O valor a ser pago será de {valorPago * 5/100}')
elif opcao == 3:
    parcelas = valorPago/2
    print(f'O valor a ser pago será de {valorPago} duas vezes em parcelas de {parcelas}')
elif opcao == 4:
    totalParc = int(input('Digite a quantidade de vezes que será pago: '))
    parcelas = valorPago / totalParc
    juros = valorPago + (valorPago * 20/100)
    print(f'{totalParc} e {parcelas}\n{juros}')
else:
    print('indisponível')