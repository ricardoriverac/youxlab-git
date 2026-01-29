resposta = 'S'
aluno = []
lista_notas = []
listad_alunos = []
i = 0
while resposta != 'N':
    aluno.clear()
    nome = str(input('Digite o nome do aluno: '))
    aluno.append(nome)
    lista_notas.clear()
    continuar_notas = 'S'
    while continuar_notas != 'N':
        nota = float(input('Digite a nota do aluno: '))
        lista_notas.append(nota)
        continuar_notas = input('Deseja adicionar mais notas [S/N]?: ').upper()

    aluno.append(lista_notas)
    listad_alunos.append(aluno.copy())
    resposta = input('Deseja adicionar mais alunos [S/N]?: ').upper()

print('→ Alunos ←')
print(" ")

for pesquisa, dados in enumerate(listad_alunos):
    print(f"{pesquisa}{dados}")
while True:
    print(" ")
    print(" - Pesquisar aluno -")
    opcao = str(input("Qual alunos deseja ver? [Digite fim para finalizar o codígo]: "))
    if opcao == "fim":
        print("Finalizado")
        break
    opcao = int(opcao)
    if opcao <= len(listad_alunos) -1:
        print(f"As notas de {listad_alunos[opcao][0]} são {listad_alunos[opcao][1]}")