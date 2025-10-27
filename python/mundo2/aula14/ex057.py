# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ""
while sexo != "M" and sexo != "F":
    sexo = input("Digite o seu sexo [M/F]: ").strip().upper()
    if sexo != "M" and sexo != "F":
        print("Erro, digite 'M' para masculino ou 'F' para feminino.")
print(f"Sexo {sexo} registrado com sucesso.")

