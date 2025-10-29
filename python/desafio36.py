valor_casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual é o salário do comprador? R$ '))
anos = int(input('Em quantos anos pretende pagar? '))
prestacao = valor_casa / (anos * 12)
limite = salario * 30 / 100
print(f'\nPara pagar uma casa de R${valor_casa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f} por mês.')
if prestacao <= limite:
    print('Empréstimo APROVADO! ')
else:
    print('Empréstimo NEGADO! ')
    print(f'A prestação excede 30% do seu salário (limite: R${limite:.2f}).')
