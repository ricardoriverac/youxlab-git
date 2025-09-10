preçoOriginal= float(input('Qual o valor do produto? ').replace('R$', ''))
FormaPagamento= str(input('Qual vai ser a forma de pagamento? ').upper())
descontoAvista= preçoOriginal-(preçoOriginal * 0.10)
descontoCartaoAvista= preçoOriginal-(preçoOriginal * 0.05)
Juros= preçoOriginal * (0.20 + 1)
if FormaPagamento == 'À vista' and FormaPagamento== 'Cheque':
    print(f'Com esta forma de pagamento, seu produto terá desconto e passará à custar {descontoAvista}')
elif FormaPagamento == 'Cartão à vista':
    print(f'Com esta forma de pagamento, seu produto terá desconto e passará  à custar {descontoCartaoAvista}')
elif FormaPagamento == 'Cartão parcelado 2x':
    print(f'Com esta forma de pagamento, seu produto terá desconto e passará  à custar {preçoOriginal}')
else:
    print(f'Com esta forma de pagamento, seu ṕroduto terá juros e passará  à custar {Juros}')

