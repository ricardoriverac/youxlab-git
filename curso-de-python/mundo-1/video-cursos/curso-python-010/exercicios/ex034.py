salario = float(input('Digite o seu salário: '))
if salario >= 1250.0:
    print(f'Você terá 10% de aumento! Você receberá {salario + (salario * 10 / 100)}')
else:
    print(f'Você terá 15% de aumento! Você receberá {salario + (salario * 15 / 100)}')