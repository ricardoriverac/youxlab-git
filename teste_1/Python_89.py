alunos = []


while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break


print('-=' * 30)
print(f'{"No.":<4} {"NOME":<10} MÉDIA')
print('-' * 26)
for i, aluno in enumerate(alunos):
    print(f'{i:<4} {aluno[0]:<10} {aluno[2]:.1f}')


while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc < len(alunos):
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
    else:
        print('Número inválido. Tente novamente.')
print('<<< VOLTE SEMPRE >>>')
