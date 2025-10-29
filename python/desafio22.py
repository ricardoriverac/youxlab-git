nome = input("Digite seu nome completo: ").strip()
# Mostra o nome em maiúsculas
print("Nome em maiúsculas:", nome.upper())
print("Nome em minúsculas:", nome.lower())
total_letras = len(nome.replace(" ", ""))
print("Total de letras (sem espaços):", total_letras)
# Conta o número de letras do primeiro nome
primeiro_nome = nome.split()[0]
print("Número de letras no primeiro nome:", len(primeiro_nome))


