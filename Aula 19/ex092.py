from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Digite seu nome: '))
ano_nasc = int(input('Digite seu ano de nascimento: '))
dados['Idade'] = datetime.now().year - ano_nasc
dados['CTPS'] = int(input('Sua carteira de trabalho (Digite 0 se não tiver): '))
if dados['CTPS'] !=0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Idade da aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f'{k} é {v}')