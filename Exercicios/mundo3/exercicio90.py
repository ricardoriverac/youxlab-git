aluno = dict()
aluno['nome'] = str(input("Digite seu nome: "))
aluno['media'] = float(input(f"Media de {aluno['nome']}: "))

if aluno['media'] > 7.0:
    aluno['situacao'] = 'Aprovado!'
else:
    aluno['situacao'] = 'Reprovado!'

print(aluno)

for chave,valor in aluno.items():
    print(f"{chave} = {valor}")

