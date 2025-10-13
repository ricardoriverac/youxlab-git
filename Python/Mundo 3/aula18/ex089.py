# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#  No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

informacoes = list()

while True:
    aluno=str(input('Nome: '))
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    media=(nota1 + nota2) / 2
    informacoes.append([aluno, [nota1, nota2], media])
    responda=(str(input('Deseja continuar[S/N]:'))).lower()
    if responda in 'Nn':
        break
print('-='*100)
print(f'{"No.":<4}{"NOME":<12}{"MÉDIA":<16}') # largura
print('-'*40)
for i, a in enumerate(informacoes): # for = repetição do i = indíce e a = aluno
    print(f'{i:<4}{a[0]:<12}{a[2]:<16.1f}')
while True:
    print('-'*40)
    numeroAluno=int(input('Mostrar notas de quais alunos? (999 interrompa)'))
    if numeroAluno == 999:
        print('Finalizando...')
        break
    if numeroAluno <=len(informacoes) -1:
        print(f'Notas de {informacoes[numeroAluno][1]}')
print('<<<< VOLTE SEMPRE!! >>>>>')
