media_peso = 0
peso = 0
resposta = ""
numero_de_pessoas = 0
pessoas = list()
pessoa = list()
print("-="*20)
print("""DIGITE SEU NOME e 
SEU PESO    """)
print("-="*20)
while True:    
    if  resposta != "sim" and resposta != "nao":
        resposta = str(input("sim ou nao? ")).lower()

    elif resposta == "sim":    
        pessoa.append(str(input("digite seu nome: ")))
        pessoa.append(float(input("digite seu peso: "))) 
        peso += peso
        numero_de_pessoas += 1
        pessoas.append(pessoa.copy())
        pessoa.clear()

        resposta = str(input(" quer continuar? sim ou nao: ")).lower()

    elif resposta == "nao": 
        break
print(numero_de_pessoas)
pessoas_pesadas = list()
pessoas_leves = list()
for p in pessoas:
    if p[1] > 90:
        pessoas_pesadas.append(p[0])
    if p[1] < 60:
        pessoas_leves.append(p[0])   
print(f"total de pessoas pesadas {pessoas_pesadas} e esse eo total de pessoas leve {pessoas_leves}")        