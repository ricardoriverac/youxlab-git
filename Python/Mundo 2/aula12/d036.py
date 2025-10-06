valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu sálario? '))
pagamento = float(input('Em quantos anos você pagará? '))
valor_prestacao = valor_casa / pagamento
maximo_prestacao = salario * 0.3
if valor_prestacao > maximo_prestacao:
    print('O empréstimo foi NEGADO!')
else:
    print('O empréstimo foi ACEITO!')

