aluno={}
aluno['nome']=str(input('Nome: '))
aluno['media']=float(input(f'Media de {aluno["nome"]}: '))


if aluno["media"] < 7:
    aluno['situacao']='Reprovado'
else:
    aluno['situacao']='Aprovado'
        
print(aluno)