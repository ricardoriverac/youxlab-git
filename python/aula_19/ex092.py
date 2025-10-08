'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Digite seu nome: '))
ano_nasc = int(input('Digite seu ano de nascimento: '))
dados['Idade'] = datetime.now().year - ano_nasc
dados['CTPS'] = int(input('Sua carteira de trabalho (Digite 0 se não tiver): '))
if dados['CTPS'] !=0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f'{k} é {v}')