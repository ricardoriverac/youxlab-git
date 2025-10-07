aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['nota1'] = int(input(f'Nota 1 de {aluno["nome"]}: '))
aluno['nota2'] = int(input(f'Nota 2 de {aluno["nome"]}: '))
aluno['media'] = aluno['nota1'] + aluno['nota2']/2
if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
else:
    aluno['situacao'] = 'REPROVADO'
print(aluno)