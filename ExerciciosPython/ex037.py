salario_mensal = float(input('Digite o seu salário mensal: '))
prestacao_desejada = float(input('Digite o valor desejado da prestação: '))

limite_maximo_prestacao = salario_mensal * 0.30

if prestacao_desejada <= limite_maximo_prestacao:
    print('Empréstimo aprovado: A prestação não excede 30% do seu salário.')
else:
    print('Empréstimo negado: A prestação excede 30% do seu salário.')