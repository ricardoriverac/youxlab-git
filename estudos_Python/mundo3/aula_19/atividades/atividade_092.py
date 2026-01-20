'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um 
dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação 
e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

#Responda

from datetime import date
dados = dict()

dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year - nascimento
dados['CTPS'] = int(input('Número da Carteira de trabalho [Digite 0 se não tiver: '))

if dados['CTPS'] != 0:
    
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = (dados['Ano de contratação'] + 35) - nascimento

for k, v in dados.items():
    print(f'{k}: {v}.')