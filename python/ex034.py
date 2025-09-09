salario = float(input('Digite o valor do seu salario: '))
aumento1 = salario * 10 /100
aumento2 = salario * 15 /100
if salario > 1250:
    total1 = aumento1 + salario
    print(f'O funcionario recebia R${salario} e agora vai receber {total1}')
else:
    total2 = aumento2 + salario
    print(f'O funcionario recebia {salario} e agora vai receber {total2}')