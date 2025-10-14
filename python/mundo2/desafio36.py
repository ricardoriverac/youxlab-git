#logica
casa = float(input('valor da acasa: R$'))
salario = float (input('salario do comprador: R$'))
anos = int(input('quantos anos de financiamento? '))
prestaçao = casa / (anos * 12)
print('para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação sera de R${:.2f}'.format(prestaçao))
#alteraçao do guanabara
casa = float(input('valor da acasa: R$'))
salario = float (input('salario do comprador: R$'))
anos = int(input('quantos anos de financiamento? '))
prestaçao = casa / (anos * 12)
minimo = salario * 30 / 100
print('para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação sera de R${:.2f}'.format(prestaçao))

print('comparando tem que pagar {} e o minimo é de {}'.format(prestaçao, minimo))
#alteração 2
casa = float(input('valor da acasa: R$'))
salario = float (input('salario do comprador: R$'))
anos = int(input('quantos anos de financiamento? '))
prestaçao = casa / (anos * 12)
minimo = salario * 30 / 100
print('para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação sera de R${:.2f}'.format(prestaçao))
if prestaçao <= minimo:
    print('empretimo pode ser CONCEDIDO')
else:
    print('emprestimo NEGADO')
print('comparando tem que pagar {} e o minimo é de {}'.format(prestaçao, minimo))
