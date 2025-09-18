# Pede ao usuário para inserir um ano
ano = int(input("Por favor, digite um ano: "))

# Verifica a lógica do ano bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")