somaidade = 0
mediaidade = 0 
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'------{p}Pessoa ------')
    nome =str(input("Digite seu nome: ")).strip()
    idade =str(input("Digite sua idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome 
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridade = idade
        nomevelho = nome 
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 2 
print (f'A média de idade do grupo é de {mediaidade} anos')
print (f'O homem mais velho tem {maioridadehomem} anos é se chama {nomevelho}')
print (f'Ao todo são {totmulher20} mulheres com menos de 20 anos')