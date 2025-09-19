valorCasa = float(input('Qual é o valor da casa: ')) 
salario = float(input('Qual o seu salário:R$ '))
prestacao = int(input('Quantidade de quantos anos que você prentende pagar: '))
totalMeses = prestacao * 12
prestacao = valorCasa / totalMeses
limitePrestacao = salario * 0.30
if prestacao <= limitePrestacao:
    print('Empréstimo APROVADO')
    print(f"Valor da casa: R$ {valorCasa:,.2f}")
    print(f"Seu salário: R$ {salario:,.2f}")
    print(f"Prestação mensal: R$ {prestacao:,.2f}")
    print(f"Este valor está dentro do limite de 30% do seu salário (R$ {limitePrestacao:,.2f}).")
else:
    print("\nEmpréstimo NEGADO.")
    print(f"A prestação mensal de R$ {prestacao:,.2f} excede o limite de 30% do seu salário, que é R$ {limitePrestacao:,.2f}.")
