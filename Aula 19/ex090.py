alunos = dict()
alunos['Nome'] = str(input('Digite o nome: '))
alunos['Media'] = float(input(f'A média do (a) aluno(a) {alunos["Nome"]} : '))
if alunos['Media'] >= 7:
    alunos['Situação'] = 'Aprovado'
elif 5 <= alunos['Media'] < 7:
    alunos['Situação'] = 'Recuperação'
else:
    alunos['Situação'] = 'REPROVADO'

print('-'*10)
for k, v in alunos.items():
    print(f'{k} é igual a {v}')
print('-'*10)