ficha = list()
resposta = ''
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('1ª nota desse aluno: '))
    nota2 = float(input('2ª nota desse aluno: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('deseja continuar?[S/N] '))
    if resposta in "Nn":
        break
print('=' * 20)
print(f'{"No.":<4}{"NOME":<7}{"MÈDIA":>7}')
for i, a in enumerate(ficha):
    print(f'{i+1:<4}{a[0]:<7}{a[2]:>7.1f}')
while True:
    aluno = int(input('Mostra notas de qual aluno?[999 para interromper programa] '))
    if aluno == 999:
        break
    if aluno <= len(ficha) - 1:
        print(f'Aluno: {ficha[aluno][0]} Notas: {ficha[aluno][1]}')
