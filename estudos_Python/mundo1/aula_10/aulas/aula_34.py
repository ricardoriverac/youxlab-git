"""
Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento.
Para salários superiores a R$1.250.00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""
#Resposta

digite_o_salario = float(input('Digite o valor do salário atual: '))

if digite_o_salario <= 1250.00 :

    e = ((digite_o_salario * 15) / 100)
    print(f'O seu novo salário e {e+digite_o_salario}')

else:

    i = (digite_o_salario / 10)
    print(f'Seu novo salário e {i+digite_o_salario}')