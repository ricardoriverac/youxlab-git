salario = float(input('QUal o salário do funcionário: '))

print(f'o salário é {salario+(salario*15/100)}' if salario < 1250 else f'O salário é {salario+(salario*0.1)}') 