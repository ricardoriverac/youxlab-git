soma_da_idade = 0 
mediaidade = 0
maioridadehomem = 0
nomevelho = ""
for c in range (0,4):
    idade = int(input("digite sua idade: "))
    sexo = str(input("digite seu sexo [masculino,feminino]: "))
    nome = str(input("digite seu nome: "))
    soma_da_idade += idade
    if c == 1 and sexo in "masculino":
        maioridadehomem = nome
        nomevelho = nome
    if sexo in "masculino" and idade > maioridadehomem:    
        maioridadehomem = idade
        nomevelho = nome 
mediaidade = soma_da_idade / 4        
print(f" a media do grupo e {mediaidade}")
print(f"a media e {mediaidade}") 
print( f"o homem mais velho tem {maioridadehomem} e se chama {nomevelho}" )  