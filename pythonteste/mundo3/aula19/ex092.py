from datetime import datetime

dados = dict()
dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nascimento
dados['CTPS'] = int(input('Carteira de trabalho(0 = não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano que foi contratado: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
print(dados)
