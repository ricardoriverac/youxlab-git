salario_pergunta = int(input('Qual é o salario do funcionario? R$ '))
novo1 = salario_pergunta + (salario_pergunta * 15)/100
novo2 = salario_pergunta + (salario_pergunta * 10)/100
if salario_pergunta <= 1250:
    print('O salario do funcionario tera aumento de {}'.format(novo1))
else: 
    print('O novo salario desse funcionario será de {}'.format(novo2))