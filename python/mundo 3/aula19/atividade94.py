minha_lista = []
resposta = "s"
pessoas = 0
media_idade = 0
media = ()
sexo_femino = 0
acima_da_media = 0

while resposta == 's':
    meu_dicionario = {}

    nome = str(input("digite seu nome: "))
    pessoas  += 1
    idade = int(input("dgite sua idade: "))

    media_idade = media_idade + idade 
    media = media_idade / pessoas
    if idade > media:
            acima_da_media += 1

    sexo = str(input("digite seu sexo [f/m] : ")).lower()
    if sexo == "f":
        sexo_femino += 1
    while sexo != "m" and sexo != "f":
        sexo = str(input("digite seu sexo [f/m] : ")).lower()
        
    meu_dicionario  = {"pessoas adicionadas": pessoas,  
    "media do grupo ":media,
    "todas mulheres" :  sexo_femino,
    "acima da media": acima_da_media}
    minha_lista.append(meu_dicionario.copy())

    resposta = str(input("quer continuar [s/n] ")).lower()  

    while resposta != "s" and resposta != "n":
        resposta = str(input("quer continuar [s/n] ")).lower()
print(meu_dicionario)            