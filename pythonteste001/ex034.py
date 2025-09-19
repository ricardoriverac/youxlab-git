salário=float(input('Qual é o salário do funcionário? R$'))
if salário<=1250.00:
    novo=salário+(salário*15/100)
else:
    novo=salário+(salário*10/100)
print('quem recebia R${:.2f} passa a ganhar R${:.2f}'.format(salário,novo))
