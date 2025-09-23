casa1 = float(input('Valor da casas: R$'))
salario = float(input('Salário do comprador: R$'))
parcela = int(input('Quantos anos de financiamento?:'))
resolucao = casa1 / (parcela * 12)
print('Para pagar uma casa de R${:.2f} em {:.2f} anos '.format(casa1, parcela,),end='')

print(',a prestação será de R${:.2f}'.format(resolucao))
