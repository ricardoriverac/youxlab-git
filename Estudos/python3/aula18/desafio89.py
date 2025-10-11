continuacao = 'S'
interrompe='999999'
Boletim= []
count=0
while continuacao == 'S':
    nome=(str(input(f'Digite o nome do aluno: ')))
    nota1=(float(input(f'Digite a primeira nota do aluno: ')))
    nota2=(float(input('Digite a segunda nota do aluno: ')))
    media= (nota1+nota2)/2
    aluno=[nome, nota1, nota2, media]
    Boletim.append(aluno)
    continuacao=str(input('Você deseja continuar? [S/N]'))

for e in enumerate(Boletim):
    print()