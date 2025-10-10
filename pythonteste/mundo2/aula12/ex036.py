casa=float(input('Valor da casa: R$'))
salário=float(input('Salário do comprador: R$'))
anos=int(input('Quantos anos de financiamento? '))
prestação=casa/(anos*12)
mínimo=salário*30/100
print('-'*100)
print('para pagar uma casa de R${:.2f} em {} anos,\na prestação será de R${:.2f}'.format(casa,anos,prestação))
if prestação<=mínimo:
    print('O empréstimo pode ser concedido!')
else:
    print('Emprestimo negado!')