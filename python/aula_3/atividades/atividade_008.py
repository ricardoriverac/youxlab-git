#Faça um algoritmo que leia o salário de um funcionário e mostre e mostre o seu novo salario, com 15% de desconto.

#Resposta 

total_do_salario = int(input('Digite o salário do funcionário : '))
calculo_da_porcentagem_do_salario = ((total_do_salario * 15 ) / 100)
soma_da_porcentagem_e_do_salario = (total_do_salario + calculo_da_porcentagem_do_salario)

print(f'O almento do salário do funcionario  e : {soma_da_porcentagem_e_do_salario}')
