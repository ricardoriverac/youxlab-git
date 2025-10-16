aluno = {}


aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))

if aluno['media'] >= 7:
    aluno['situacao'] = '\033[32mAprovado!\033[m'
else:
    aluno['situacao'] = '\033[31mReprovado!\033[m'

for k, v in aluno.items():
    print(f'Nome é {v}')
    print(f'A média de {k} é {v}')
    print(f'Situação é igual a {aluno["situacao"]}')
    break