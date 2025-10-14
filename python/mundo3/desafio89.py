nomes = []
nota_1 = []
nota_2 = []
while True:
    nome = str(input('NOME: '))
    n1 = float(input('NOTA 1: '))
    n2 = float(input('NOTA 2: '))
    nomes.append(nome)
    nota_1.append(n1)
    nota_2.append(n2)
    print(nota_1)
    print(nota_2)
    print(nomes)
    resposta = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if resposta in 'N':
        break
print('=' * 35)
print(f'{"No.":<5}{"NOME":<16}MÉDIA')
print('_'* 35)
for p, n in enumerate(nomes):
    media = (nota_1[p] + nota_2[p]) / 2
    print(f'{p:<5}{n:<16}{media:.1f}')
print('_' * 35)
while True:
        nota = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
        if nota == 999:
            print('-' * 35)
            print('Finalizando...')
            break
        print()
        print('=' * 35)
        print(f'Notas de {nomes[nota]} são: {[nota_1[nota], nota_2[nota]]}')
        print('=' * 35)
        print()
print('Volte sempre!')