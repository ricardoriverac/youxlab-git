lista = []
while True:
    nome = str(input('Digite o Nome: ')).title()
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda Nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    perg = str(input('Deseja continuar? (S/N): '))
    if perg in 'nN':
        break
print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, n in enumerate(lista):
    print(f'{i:<4}{n[0]:<10}{n[2]:>8}')
while True:
    print('-'*35)
    escolha = str(input('Quer ver a nota de qual aluno? (999) para sair. '))
    if escolha in '999':
        print('Sistema encerrado com Sucesso..')
        break
    if escolha <= len(lista) - 1:
        print(f'Notas de {lista[escolha][0]} são {lista[escolha][1]}')
print('<<<< VOLTE SEMPRE >>>>')