pessoa = {} 
pessoa['nome'] = str(input("Digite seu nome: "))
pessoa['ano de nascimento'] = int(input(f"Ano de nascimento de {pessoa['nome']}: "))
pessoa['carteira de trabalho'] = int(input(f"Carteira de trabalho de {pessoa['nome']} (0 -> não tem): "))
pessoa['idade'] = 2025 - pessoa['ano de nascimento']

# Se a pessoa tiver carteira de trabalho pede os dados adicionais
if pessoa['carteira de trabalho'] != 0:
    pessoa['ano de contratacao'] = int(input(f"Ano de contratação de {pessoa['nome']}: "))
    pessoa['salario'] = float(input(f"Salário de {pessoa['nome']}: R$ "))
    
    # Calcula os anos que já contribuiu
    anos_contribuidos = 2025 - pessoa['ano de contratacao']
    # Calcula quanto ainda falta até 45 anos de contribuição
    falta_contribuir = 45 - anos_contribuidos
    # Calcula a idade de aposentadoria
    pessoa['idade de aposentadoria'] = pessoa['idade'] + falta_contribuir
