from datetime import date
anoAtual = (date.today().year)
dados = {}
while True:
    dados['Nome'] = str(input('Insira o seu nome: '))
    dados['AnoDeNascimento'] = int(input('Insira o seu ano de nascimento: '))
    dados['CTPS'] = int(input('Insira o número da Carteira\nSe não possuir insira o número 0'))
    if dados['CTPS'] <= 0:
        print('Você não trabalha!')
    anoDoContrato = int(input('Insira o ano da contratação: '))
    if anoAtual - anoDoContrato > 35:
        dados['AnoDaContratacao'] = anoDoContrato
    else:
        anosQueFaltam = anoDoContrato - anoAtual + 35
        print(f'Ainda faltam {anosQueFaltam} anos para se aposentar!')
    dados['Salário'] = float(input('Insira o seu salário: '))
    dados['Aposentadoria'] = anoDoContrato + 35
    break
for k, v in dados.items():
    print (f'{k} - {v}')