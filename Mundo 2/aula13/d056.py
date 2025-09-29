somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0
for pessoa in range(1, 5):
    print(f'----- {pessoa}º PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [Masc/Femin]: ')).strip()
    somaidade += idade
    if pessoa == 1 and sexo in 'Masculino':
        maioridadehomem = idade 
        nomevelho = nome
    elif sexo in 'Masculino' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    elif sexo in 'Feminino' and idade < 20:
        totalmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totalmulher20} mulheres com mais de 20 anos.')