salario = float(input('Qual o salario do profissional?'))
aumento = float(input('Qual o valor do aumento? [%] '))
print(f'O profissional que ganhava {salario :2} com aumento de {aumento:2}% passara à ganhar {salario +(aumento*salario/100):2}')

