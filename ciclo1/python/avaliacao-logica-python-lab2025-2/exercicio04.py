def analisar_aluno(nome, notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    return {"nome": nome, "media": media, "situacao": situacao}

alunos = []

for nome_aluno in range(3):
    nome = str(input("Qual o nome do aluno(a): "))
    
    notas = []
    for notas_aluno in range(3):
        nota = float(input(f'Qual a {notas_aluno+1}° nota do(a) {nome}: '))
        notas.append(nota)
        
    aluno = analisar_aluno(nome, notas)
    alunos.append(aluno)

print(" ")
print("→ Dicionário de alunos ←")
for aluno in alunos:
    print(f"Nome:{aluno['nome']}")
    print(f"Média:{aluno['media']:.2f}")
    print(f"Situação:{aluno['situacao']}")