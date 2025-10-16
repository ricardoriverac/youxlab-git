clt={}
clt['nome']=str(input('Digite o nome da pessoa: '))
clt['ano_de_nascimento']=int(input('Digite o ano de nascimento: '))
clt['numero_da_CTPS']=float(input('Digite o numero da CTPS: '))

if clt['numero_da_CTPS'] != 0:
    clt['ano_de_contratacao']=int(input('Digite o ano de contratação: '))
    clt['salario']=float(input('Digite o salario: '))
    anoDeAposentadoria = 35 + clt['ano_de_contratacao']
    FaltaMuito = anoDeAposentadoria - 2025
else:
    print('O valor da carteira foi 0')      
    
idade = 2025 - clt['ano_de_nascimento']

if clt['numero_da_CTPS'] == 0:
    print(f'O nome é {clt["nome"]}, ele tem {idade} e o numero da sua carteira é {clt["numero_da_CTPS"]}' )
else:
    print(f'O nome é {clt["nome"]}, ele tem {idade} anos e o numero da sua carteira é {clt["numero_da_CTPS"]},o salario é {clt["salario"]} e falta {FaltaMuito} anos pra ele aposentar.')
print(clt)