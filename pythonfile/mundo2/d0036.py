casa = float(input('Qual o valor da casa? : '))
salario = float(input('Qual o seu salario? : '))
prestacao = int(input('Em quantos anos você quer pagar a casa? : '))
max_prestacao = salario *0.3
valor_prestacao = casa/(prestacao *12)
if valor_prestacao > max_prestacao:
    print('Você não pode realizar o emprestimo')
else:
    print('Você consegue realizar o emprestimo')