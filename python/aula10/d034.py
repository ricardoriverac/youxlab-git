salario = float(input('Digite seu salário: '))
salario2 = salario * 1.10
salario3 = salario * 1.15
if salario > 1250:
    print(f'Seu salário com 10% de aumento é: {salario2:.2f}')
elif salario <= 1250:
    print(f'Seu salário com 15% de aumento é: {salario3:.2f}')
