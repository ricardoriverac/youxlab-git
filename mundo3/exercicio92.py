dici = {}

dici['nome'] = str(input('Nome: '))
anodn = int(input('Ano de nascimento: '))
dici['idade'] = 2025 - anodn
dici['carteira'] = int(input('Carteira de trabalho (0 para nenhuma): '))
if dici['carteira'] != 0:
    dici['ano de contratação'] = int(input('Ano de contratação: '))
    apo = 2025 - dici['ano de contratação']
    dici['salario'] = int(input('Salario: R$ '))
else:
    pass

print (dici)
print (f'O nome tem o valor {dici["nome"]}')
print (f'A idade tem o valor {dici["idade"]}')
if dici['carteira'] != 0: 
    print (f'A ctps tem o valor {dici["carteira"]}')
    print (f'Contratação tem o valor {dici["ano de contratação"]}')
    print (f'O salalrio tem o valor {dici["salario"]}')
    print (f'A aposetadoria é {apo}')

