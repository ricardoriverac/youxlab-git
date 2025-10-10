pessoas = []
mulheres = []

while True:
    nome = input("Nome: ")
    sexo = input("Sexo [M/F]: ").strip().upper()
    idade = int(input("Idade: "))

    pessoa = {'nome': nome, 'sexo': sexo, 'idade': idade}
    pessoas.append(pessoa)

    if sexo == 'F':
        mulheres.append(nome)

    continuar = input("Quer continuar? [S/N]: ").strip().upper()
    if continuar == 'N':
        break

# Exibir dados
print("-=" * 30)
print(f"A) Total de pessoas cadastradas: {len(pessoas)}")

# media = sum(p['idade'] for p in pessoas) / len(pessoas) <- explicar
print(f"B) Média de idade: {media:.2f} anos")

# print(f"C) Mulheres cadastradas: {', '.join(mulheres) if mulheres else 'Nenhuma'}")

print("D) Pessoas com idade acima da média:")
for p in pessoas:
    if p['idade'] > media:
        print(f"   Nome = {p['nome']}; Sexo = {p['sexo']}; Idade = {p['idade']}")

print("<< ENCERRADO >>")