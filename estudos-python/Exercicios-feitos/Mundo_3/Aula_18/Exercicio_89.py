listaDeAlunos = []
aluno = []
notas = []
numeroDoAluno = 0
quantidadeAluno = int(input('Escolha a quantidade de alunos: '))
for c in range (quantidadeAluno):
    nome = input('Coloque o nome do aluno: ')
    nota1 = float(input('Insira a primeira nota: '))
    nota2 = float(input('Insira a segunda nota: '))
    media = (nota1 + nota2) / 2
    notas.append(nota1)
    notas.append(nota2)
    aluno.append(nome)
    aluno.append(notas[:])
    listaDeAlunos.append(aluno[:])
    notas.clear()
    aluno.clear()
for i in listaDeAlunos:
    print(f'Os alunos escolhidos foram : {i[0]}\nE sua médias de notas foram respectivamente:\n{(i[1][0]+i[1][1])/2}')
opcao = input('Você gostaria ver as notas individuais de algum aluno?\nSe sim digite S ou s: ').strip().upper()
counter = 0
while opcao == 'S':
    for p in listaDeAlunos:
        print(f'{p[0]} -> {counter}')
        counter += 1
    escolha = int(input('Qual aluno você gostaria de ver as notas?'))
    print(listaDeAlunos[escolha][1])
    opcao = input('Você gostaria de continuar?\nSe sim, digite S ou s: ').strip().upper()
print = ('-'*5'|FIM|''-'*5)