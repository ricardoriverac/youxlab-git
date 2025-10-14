# criando uma lista para guardar os dados dos alunos
boletim = []

# começa um laço infinito, vai repetir até eu usar o break.
while True:

#input() pede o nome.
#.strip() tira espaços extras.
#.title() deixa a primeira letra maiúscula (tipo: "emily alves" vira "Emily Allves").
    n = str(input('Qual o nome do aluno? ')).strip().title()

# pede as duas notas
#As duas notas são salvas como números decimais (por isso float()).
    note = float(input('Qual a nota do aluno? '))
    note2 = float(input('Qual a segunda nota do aluno? '))

# calculando a média: soma duas notas e divide por 2.
    média = (note + note2) / 2

#guarda todos os dados do aluno na lista boletim
    boletim.append([n, [note, note2], média])

# pergunta se quer adicionar outro aluno
    perg = str(input('Deseja resgistrar outro aluno? [S/N] ')).strip().upper()[0]
    
# Se a resposta não for "S" ou "N", ele avisa / da erro.
    if perg not in 'SN':
        print('\033[33mNão entendi...', end=' ')

#se for nao a resposta, ele para o programa.
        perg = str(input('[Responda com [S/N]: ')).strip().upper()[0]
        if perg == 'N':
            break
    if perg == 'N':
        break

#mostra o boletim:
print('-=' * 5, 'BOLETIM', '=-' * 5)
print(f'{"Nº":<4}{"NOME ":<10}{"NOTA":>8}')
print('-' * 25)

#ele mostra aluno com todos os dados.
for i, aluno in enumerate(boletim):
   print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8}')

#mostra as notas
while True:
    continuar = int(input('Digite o número do aluno para ver a nota (999 para parar): '))
    if continuar == 999:
        break
    if continuar <= len(boletim):
        print(f'As notas do aluno {boletim[continuar][0]} são {boletim[continuar][1]}')
