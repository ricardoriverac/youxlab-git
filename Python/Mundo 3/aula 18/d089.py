ficha = []
resposta = 'S'
print('-'*26)
print('    BOLETIM ESCOLAR    ')
print('-'*26)
while resposta == 'S':
    aluno = str(input('-> Nome do aluno: '))
    primeiraNota = float(input('-> Primeira nota: '))
    segundaNota = float(input('-> Segunda nota: '))
    media = (primeiraNota + segundaNota) / 2
    ficha.append([aluno, [primeiraNota, segundaNota], media])
    resposta = str(input('...Deseja continjuar? [S/N]: ')).upper().strip()
    print('-'*26)
    if resposta == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA:>8"}')
print('-'*26)
for ind, alu in enumerate(ficha):
    print(f'{ind:<4}{alu[0]:<10}{alu[2]:>8.1f}')
print('-'*26)
while True:
    print('-='*26)
    opc = int(input('-> Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('-'*26)
        print('''FINALIZANDO...''')
        print('-'*26)
        break
    if opc <= len(ficha) - 1:
        print(f'-> Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<  VOLTE SEMPRE  >>>')