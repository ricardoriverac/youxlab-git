salario = float(input('Qual o valor do seu salario ? '))
if salario > 1250.00:
    salamaior = salario*10/100
    print ('O almento do seu salário será {} '.format(salamaior + salario))
else:
    salamenor = salario*15/100
    print ('seu salário atual será {}'.format(salamenor + salario))