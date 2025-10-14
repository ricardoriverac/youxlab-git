from datetime import date  # Importa a função 'date' para pegar o ano atual automaticamente

dados = {}  # Cria um dicionário vazio para armazenar as informações do cidadão

# Pede o nome do cidadão, tira espaços e deixa com a primeira letra maiúscula
dados["Nome"] = str(input("Nome do cidadão: ")).strip().title()

# Pede o ano de nascimento e armazena como número inteiro
AnoNasc = int(input("Ano de Nascimento: "))

# Pega o ano atual (ex: 2025)
AnoAtual = date.today().year

# Calcula a idade do cidadão, ano de nascimento menos ano atual
dados["Idade"] = AnoAtual - AnoNasc 

# Pede o número da carteira de trabalho (CTPS). Se for 0, significa que não tem
dados["Carteira"] = int(input("Número da carteira de trabalho (0 caso não tenha): "))

# Verifica se a pessoa tem carteira de trabalho / se digitou um número diferente de 0
if dados["Carteira"] != 0:
    # Se tiver CTPS, pede o ano de contratação e o salário
    dados["Ano de contratação"] = int(input("Ano de contratação: "))
    dados["Salário"] = float(input("Salário do funcionário:R$ "))

    # Calcula o ano em que a pessoa pode se aposentar (dps de 35 anos de trabalho)
    AnoAposentadoria = dados["Ano de contratação"] + 35

    # Calcula a idade que a pessoa terá no ano da aposentadoria
    IdadeAposentadoria = AnoAposentadoria - AnoNasc

    # Armazena a idade da aposentadoria no dicionário
    dados["Aposentadoria"] = IdadeAposentadoria

    # Mostra todas as informações formatadas
    print("="*55)
    print(f'''    - NOME: {dados["Nome"]}
    - IDADE: {dados["Idade"]}
    - CTPS: {dados["Carteira"]}
    - Ano de contratação: {dados["Ano de contratação"]}
    - Salário: R${dados["Salário"]}
    - Idade da aposentadoria: {dados["Aposentadoria"]}''')

else:
    # Se não tiver CTPS, mostra apenas nome, idade e diz que está desempregado
    print("="*55)
    print(f'''    - NOME: {dados["Nome"]}
    - IDADE: {dados["Idade"]}
    - CTPS: Não possui, o cidadão está desempregado''')
