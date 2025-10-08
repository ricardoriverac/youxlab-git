resp = 'S'
cadastro = []
dados = {}
anoAtual = 2025
while resp == 'S':
    dados['Nome'] = str(input('-> Nome: '))
    dados['Ano de Nascimento'] = int(input('-> Ano de Nascimento: '))
    idade = anoAtual - dados["Ano de Nascimento"]
    dados['Carteira de Trabalho'] = int(input('-> CTPS (Carteira de Trabalho): '))
    cadastro.append(dados["Nome"])
    cadastro.append(idade)
    cadastro.append(dados['Carteira de Trabalho'])
    if dados['Carteira de Trabalho'] != 0:
        dados['Ano de Contratação'] = int(input('-> Ano de contratação: '))
        dados['Salario'] = float(input('Salário: '))
        cadastro.append(dados['Ano de Contratação'])
        cadastro.append(dados['Salário'])
        aposentadoria = dados['Ano de Contratação'] + 35
        aposentadoria = dados['Ano de Contratação'] - dados['Ano de Nascimento']
        cadastro.append(aposentadoria)
        print(f'nome : {cadastro['Nome']}\n idade: {cadastro['idade']}\n ctps: {cadastro['Carteira de trabalho']}\n salario: {cadastro['Salario']} ')
        resp = str(input('Digite N para sair: '))
        if resp == 'N':
            print('FINALIZANDO...')
