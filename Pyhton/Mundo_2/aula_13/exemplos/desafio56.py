somadaidade = 0
mediadaidade = 0
maioridadedehomem = 0
homemvelho = " "
mulher20 = 0
for c in range (1,5):
    print(f'{c}ª pessoa')
    nome = str(input(f'Digite o nome da {c}ª pessoa: '))
    idade = int(input(f'Digite a idade da {c}ª pessoa: '))
    sexo = str(input(f'Digite o sexo da {c}ª pessoa: [feminino/masculino]')).strip()
    somadaidade += idade
    if c == 1 and sexo in 'masculino':
        maioridadedehomem = idade
        homemvelho = nome
    if sexo in 'masculino' and idade > maioridadedehomem:
        maioridadedehomem = idade 
        homemvelho = nome
    if sexo in 'feminino' and idade < 20:
        mulher20 = mulher20 + 1
mediadaidade = somadaidade / 4
print(f'A média de idade é de {mediadaidade} anos.')
print(f'O homem mais velho se chama {homemvelho} e tem {maioridadedehomem} de idade')
print(f'No total tem {mulher20} mulheres com menos de 20 anos')