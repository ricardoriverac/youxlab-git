salario = float(input('Qual é o seu salario? R$'))
aumento1 = salario + (salario*10 / 100)
aumento2 = salario + (salario*15/100)
if salario>1250:
    print(f'Seu salário novo é de: R${aumento1}')
else:
    print(f'Seu salário novo é de: R${aumento2}')