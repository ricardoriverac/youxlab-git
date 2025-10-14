# Pede o nome do aluno e remove espaços antes e depois
nome = str(input("Nome: ")).strip()

# Pede a média do aluno (convertida para número decimal)
media = float(input(f"Média de {nome}: "))

# Cria um dicionário com os dados do aluno: nome e média
dic1 = {"nome" : nome, "media" : media}

# Mostra o nome do aluno que ta guardado no dicionário
print(f'     - nome é igual a {dic1["nome"]}')

# Mostra a média do aluno que ta guardada no dicionário
print(f'     - média é igual a {dic1["media"]} ')

# se a média for menor que 7, está em recuperação
if dic1["media"] < 7:
    print("     - Recuperação")
else:
    # Se for 7 ou mais, está aprovado
    print("     - Aprovado")