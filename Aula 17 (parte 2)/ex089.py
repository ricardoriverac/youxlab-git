dadosalunos = []
notas = []
media = []
while True:
    nome = str(input('Nome: ')).strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2) / 2
    notas.append(nome)
    media.append(m)
    notas.append(media[:])
    notas.append(n1)
    notas.append(n2)
    dadosalunos.append(notas[:])
    media.clear()
    notas.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    while resp not in 'SsNn':
        resp = str(input('Resposta inválida. Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print(dadosalunos)
print('-='*15)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for p, v in enumerate(dadosalunos):
    print(f"{p:<4}{v[0]:<10}{v[1][0]:>8.1f}")
print('-'*30)
while True:
    perg = int(input('Deseja ver as notas de qual aluno? (999 interrompe): '))
    if perg <= len(dadosalunos) - 1:
        print(f'As notas de {dadosalunos[perg][0]} são {dadosalunos[perg][2]} e {dadosalunos[perg][3]}')
    if perg == 999:
        print('FINALIZANDO...')
        print('VOLTE SEMPRE!')
        break
    print('-'*30)