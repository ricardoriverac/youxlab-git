'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No 
final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas 
de cada aluno individualmente.
'''

#Resposta

alunos = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    alunos.append({'nome': nome, 'notas': [nota1, nota2], 'media': media})

    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')


for i, aluno in enumerate(alunos):
    print(f'{i:<4}{aluno["nome"]:<10}{aluno["media"]:>8.1f}')


while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        print('FINALIZANDO...')
        break
    
    if 0 <= opcao < len(alunos):
        print(f'Notas de {alunos[opcao]["nome"]}: {alunos[opcao]["notas"]}')
    else:
        print('Número inválido, tente novamente.')
print('volte sempre')
