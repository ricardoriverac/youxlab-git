boletim = []

print('------CADASTRO DE ALUNOS E NOTAS-------')

for i in range(2):
    nome = input(f'Digite o nome do {i+1}° aluno: ').title()
    nota1 = float(input('Digite a 1ª nota: '))
    nota2 = float(input('Digite a 2ª nota: '))
    nota3 = float(input('Digite a 3ª nota: '))
    nota4 = float(input('Digite a 4ª nota: '))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    boletim.append([nome, [nota1, nota2, nota3, nota4], media])

print('\n--- Boletim dos Alunos ---')
for i in range(len(boletim)):
    print(f'{i} - Aluno: {boletim[i][0]} | Média: {boletim[i][2]:.1f}')

indice = int(input('\nDigite o número do aluno para ver as notas: '))

print(f'Aluno: {boletim[indice][0]}')
print(f'Notas: {boletim[indice][1]}')
print(f'Média: {boletim[indice][2]:.1f}')
