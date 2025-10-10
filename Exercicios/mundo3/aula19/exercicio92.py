pessoa = dict()

pessoa['nome'] = str(input("Digite seu nome: "))
pessoa['ano_de_nascimento'] = float(input(f"ano de nascimento de {pessoa['nome']}: "))
pessoa['carteira_de _trabalho'] = float(input(f"carteira de trabalho de {pessoa['nome']} (0 -> não tem): "))

if pessoa['carteira_de _trabalho'] != 0:
    pessoa['ano_de_contratacao'] = float(input(f"Ano de contratação de {pessoa['nome']}: "))
    pessoa['salario'] = float(input(f"Salario de {pessoa['nome']}: R$ "))

pessoa['idade'] = 2025 - pessoa['ano_de_nascimento']
pessoa['idade_de_aposentadoria'] = (45 - (2025 - pessoa['ano_de_contratacao']))  + pessoa['idade']
print(pessoa)

