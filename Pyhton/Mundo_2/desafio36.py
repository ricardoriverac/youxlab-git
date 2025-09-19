#criando as variaveis
casa = int(input('Digite o valor da casa: '))
salario = int(input('Digite o valor do salário do comprador: '))
pagamento = int(input('Em quantos anos irá pagar? '))
valor_prestacao = casa / pagamento
maximo_prestacao = salario * 0.3
if valor_prestacao > maximo_prestacao:
    print('Seu emprestimo foi negado.')
else:
    print('Seu emprestimo foi aceito')