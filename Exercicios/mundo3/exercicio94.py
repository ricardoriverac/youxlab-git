resposta = "S"
pessoas = []
contador = 0
soma = 0
dados = dict()
mulheres = []
acima_media = []
while resposta == "S":
    dados.clear()
    dados['nome']= str(input("Qual o seu nome?: "))
    dados['sexo'] = str(input("Qual o seu sexo? [F/M]: ")).upper()
    dados['idade'] = int(input("Digite sua idade: "))
    resposta = str(input("Deseja continuar? [S/N]: ")).upper()
    pessoas.append(dados)
    contador += 1
    soma += dados['idade']
    while resposta != "S" and resposta != "N":
        resposta = str(input("Deseja continuar? [S/N]: ")).upper()
        
    media = soma / contador   
for idade in pessoas:
    if idade['idade'] > media:
        acima_media.append(idade['idade'])

for pessoa in pessoas:
    if pessoa['sexo'] == "F":
        mulheres.append(pessoa['nome'])
print(soma)
print(media)
print(acima_media)
print(mulheres)