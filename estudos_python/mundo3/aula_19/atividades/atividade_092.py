'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um 
dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação 
e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

#Responda

import datetime
data_atual = datetime.date.today()
ano_atual = data_atual.year
print(ano_atual)

nome = str(input('Digite o seu nome: '))
ano_nascimento = int(input('Digite o ano em que você nasceu: '))
idade = ano_atual - ano_nascimento
carteira_de_trabalho = int(input('Qual a sua carteira de trabalho(0, não tem): '))
dados = { 'Nome':nome , 'Ano_de_nascimento':ano_nascimento , 'Carteira_de_trabalho':carteira_de_trabalho}
print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'''
Nome: {dados["Nome"]}
Idade: {idade}
Ctps: {dados["Carteira_de_trabalho"]}''')
if carteira_de_trabalho != 0: