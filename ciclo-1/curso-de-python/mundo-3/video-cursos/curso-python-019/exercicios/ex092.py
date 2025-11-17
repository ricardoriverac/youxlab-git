import datetime 

informacaoGeral = {}

informacaoGeral['nome'] = str(input('Nome: '))
informacaoGeral['nascimento'] = int(input('Ano de Nascimento: '))
informacaoGeral ['idade'] = datetime.date.today().year - informacaoGeral['nascimento']
informacaoGeral['ctps'] = int(input('CTPS: '))
del informacaoGeral['nascimento']

if informacaoGeral['ctps'] != 0:
    informacaoGeral['contratacao'] = int(input('Ano de Contratação: '))
    informacaoGeral['salario'] = float(input('Salário: '))
    informacaoGeral['aposentarria'] = (datetime.date.today().year - informacaoGeral['contratacao']) + 35

print('-' * 25)

for k, v in informacaoGeral.items():
    print(f'{k} tem o valor {v}')