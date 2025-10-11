alunos=dict()
while True:
    alunos['nome']= str(input('Digite o nome do aluno: '))
    alunos['media']=float(input(f'Digite a média de {alunos["nome"]}: '))
    nome= alunos["nome"]
    media=alunos["media"]
    print(f'O aluno se chama {nome}', end='')
    print()
    print(f'A media de {nome} é {media}')
    if alunos['media'] > 3 and alunos['media'] < 7:
        print(f'Ele está em recuperação final')
    if alunos['media'] < 3:
        print(f'REPROVADO!')
    else:
        print(f'Aprovado!')