aluno = {}
boletim = []
for c in range(0, 3):
    aluno['nome'] = str(input('Nome: '))
    aluno['nota1'] = int(input('Nota 1: '))
    aluno['nota2'] = int(input('Nota 2: '))
    aluno['media'] = aluno['nota1'] + aluno['nota2']/2
    if aluno['media'] >= 7:
        aluno['situacao'] = 'APROVADO'
    else:
        aluno['situacao'] = 'REPROVADO'
    boletim.append(aluno.copy())
print(boletim)