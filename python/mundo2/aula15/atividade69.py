anos18 = homens =  mulheres20 = 0
condicao = 1
sexo = ""
while condicao != 0:
    idade = int(input("digite sua idade: "))
    if idade >= 18:
        anos18 += 1
        while condicao != 0: 
            sexo = str(input("digite seu sexo: [m/f]" )).lower()
            if sexo != "m" and sexo != "f":
                anos18 -= 1
                break
            if sexo == "m":
             homens += 1
            if sexo == "f" and idade < 20:
                mulheres20 += 1    
            condicao = int(input("quer continuar [0 para /1 continua]")) 
            if condicao == 0:
                break
print(f"o total de pessoa com mais de 18 anos foi {anos18},homens com mais de 18 foi {homens} e mulheres com menos de 20 anos foi {mulheres20} ")    