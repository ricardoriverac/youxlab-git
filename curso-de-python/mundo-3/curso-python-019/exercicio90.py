aluno = {} #dicionario
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média do(a) {aluno["nome"]}: '))
if aluno['média'] >= 6:
    print('aprovado')
elif 5 <= aluno['média'] < 6:
    print('recuperação')
else:
    print('reprovado')