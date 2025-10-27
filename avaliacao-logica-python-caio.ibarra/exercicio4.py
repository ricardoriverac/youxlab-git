boletim = []
notas = []
print('-------CADASRTRO DE ALUNO-------')
while True:
    nome = str(input('Nome do aluno:'))
     
    for i in range(4):
        nota = float(input(f'Nota {i+1}:'))
        notas.append(nota)
    media = sum(notas) / 4

    if media >= 7:
        situacao = 'Aprovado'

    elif media >= 5:
        situacao = 'Recuperacao'

    else:
        situacao = 'Reprovado'

    boletim.append({"nome": nome, "notas": notas, "media" : media, "situacao" : situacao})

    continuar = str(input('Deseja cadastrar outro aluno? [S/N]:')).upper()
    if continuar == "N":
        break

print("\n------ BOLETIM COMPLETO ------")
for i, aluno in enumerate(boletim):
    print(f"{i} - {aluno['nome']} | Média: {aluno['media']:.1f} | {aluno['situacao']}")

indice = int(input("\nDigite o número do aluno para ver as notas: "))
print(f"Nome: {boletim[indice]['nome']}")
print(f"Notas: {boletim[indice]['notas']}")
print(f"Média: {boletim[indice]['media']:.1f}")
print(f"Situação: {boletim[indice]['situacao']}")


    