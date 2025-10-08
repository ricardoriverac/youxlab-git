resposta = "S"
pessoas = []
contador = 0
mulheres = {}
while resposta == "S":
    dados = dict()
    dados['nome']= str(input("Qual o seu nome?: "))
    dados['sexo'] = str(input("Qual o seu sexo? [F/M]: ")).upper()
    dados['idade'] = str(input("Digite sua idade: "))
    pessoas.append(dados)
    contador += 1
    resposta = str(input("Deseja continuar? [S/N]: ")).upper()
    while resposta != "S" and resposta != "N":
        resposta = str(input("Deseja continuar? [S/N]: ")).upper()

nome_mulheres = []
for nome, pessoas in dados.items():
    if dados.get('sexo') == "F":
        nome_mulheres.append(nome)
    
print(pessoas)
print(f"Foram cadastradas {contador} pessoas!")
print(f"As mulheres foram {nome_mulheres}")

    
