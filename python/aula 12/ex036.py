valor_da_casa = float(input('qual é o valor da casa? '))
salario_comprador = float(input('Qual é o salario do comprador? '))
anos_pagamento = int(input('Em quantos anos você vai pagar? '))
prestacao = valor_da_casa / (anos_pagamento * 12) 
if prestacao <= (salario_comprador * 0.3):
    print(f'O empréstimo foi concedido no valor de {prestacao}')
else:
    print('O empréstimo foi negado')