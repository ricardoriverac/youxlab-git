informacoes= {}
informacoes['Nome']= str(input('Digite seu nome: '))
informacoes['Ano de Nascimento']= int(input('Qual seu ano de nascimento? '))
informacoes['Carteira de Trabalho']=int(input('Qual o número da sua carteira de trabalho? (Digite 0 se não possuir)'))
if informacoes['Carteira de Trabalho'] != 0:
    informacoes['Ano de Contratação']=int(input('Qual o ano de contratação? '))
    informacoes['Salario']=float(input('Qual seu salario? '))
    informacoes['Aposentadoria']='65'
if informacoes['Carteira de Trabalho'] == 0:
    informacoes.pop('Carteira de Trabalho')
for i, v in enumerate (informacoes.items()):
    print(f'Seu {v[0]} tem valor {v[1]}')