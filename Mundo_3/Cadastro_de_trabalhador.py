from datetime import datetime
lista = []
dados = {}
dados['Nome'] = str(input('nome: ')).title().strip()
anon = int(input('Digite o ano de nascimento (Ex: 1985): '))
dados['Idade'] = datetime.now().year - anon
ctps = int(input('Digite a carteira de trabalho (0 não tem): '))
if ctps != '0':
    dados['Ctps'] = ctps
    dados['Ano de Contratação'] = int(input('Digite o ano de contratação: '))
    dados['Salário'] = float(input('Digite o Salário atual: '))
    dados['aposentadoria'] = dados['Idade'] + dados['Ano de Contratação'] + 35 - datetime.now().year
lista.append(dados.copy())
print('-='*30)
for k, v in dados.items():
    print(f'- {k} é {v}.')