resposta = "Sim"
contador_maior18 = 0
contador_homens = 0
contador_mulher = 0

while resposta == "Sim":
    idade = int(input("Qual a sua idade?: "))
    sexo = str(input("Qual o seu sexo [F/M]: ")).upper()
    if idade > 18:
        contador_maior18 += 1
    if sexo == "M":
        contador_homens += 1
    else:
        if idade < 20:
            contador_mulher += 1
    resposta = input("Você deseja continuar? [S/N]: ")
print(f"Ha {contador_maior18} com mais de 18 anos, {contador_homens} cadastrados e {contador_mulher} com menos de 20 anos!")