salario = float(input('Digite o valor do seu salário:R$ '))
if salario >= 1250.00:
    valorAumento = 0.10
    aumento = salario*valorAumento
    novoSalario = salario+aumento
    print(f'Seu salário aumentou para R${novoSalario}')
else:
    salario <= 1250.00
    valorAumento = 0.15
    aumento = salario*valorAumento
    novoSalario = salario+aumento
    print(f'Seu salário aumentou para R${novoSalario}')
