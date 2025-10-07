aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média do {aluno["nome"]}: '))

if aluno['média'] >= 7:
    print('aprovado')
elif 5 <= aluno['média'] < 7:
    print('recuperação')
else:
    print('reprovado')