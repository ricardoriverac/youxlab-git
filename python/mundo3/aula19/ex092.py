#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime
ano_atual = datetime.date.today().year
trabalhador = {}
trabalhador ["nome"] = input('Digite seu nome: ')
ano_nasci_str = (input('Digite o ano em que você nasceu: '))
trabalhador["ano_nascimento"] = int (ano_nasci_str)
trabalhador['idade'] = ano_atual - trabalhador['ano_nascimento']
ctps_str = input('Número da CTPS (Digite 0 caso não tiver): ')
trabalhador['ctps'] = int(ctps_str)
if trabalhador['ctps'] != 0:
    ano_contrato_str = (input('Digite o ano de contrataçaõ: '))
    salario_str = (input('Digite o salário: '))
    trabalhador['ano_contrato'] = int(ano_contrato_str)
    trabalhador['salario'] = float(salario_str)
    trabalhador['aposentadoria_ano'] = trabalhador['ano_contrato'] + 35
    trabalhador['aposentadoria_idade'] = trabalhador['idade'] + (trabalhador['aposentadoria_ano'] - ano_atual)
print('---DADOS DO TRABALHADOR---')
for c, v in trabalhador.items():
    print(f'{c.capitalize()}: {v}')


