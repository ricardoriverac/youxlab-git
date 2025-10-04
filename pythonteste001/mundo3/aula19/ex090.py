aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Media'] >+ 7:
    aluno['Situacao'] = 'Aprovado'
elif aluno['Media'] >= 5 and aluno['Media'] < 7:
    aluno['Situacao'] = 'em Recuperação'
else:
    aluno['Situacao'] = 'Reproado'
print(f'aluno {aluno["Situacao"]}')