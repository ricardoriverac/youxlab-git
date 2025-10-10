somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher = 0
for p in range(1, 5):
    nome =str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade'))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and  idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher += 1
mediaidade = somaidade / 4 
print(f'A media de idade do grupo é de {mediaidade}')
print(f'O Homem mais velho do grupo tem {maioridadehomem} e se chama {nomevelho} ')
print(f'Ao todo são {totalmulher} mulher com menos de 20 anos')