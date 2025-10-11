dicionário = dict()
lista = list()
média = cont =  0
while True:
    dicionário['nome'] = str(input('Nome:')).strip().title()
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo: [M/F]')).strip().lower()[0]
    if sexo == 'm':
        dicionário['sexo'] = sexo
    else:
        dicionário['sexo'] = sexo
    idade = int(input('Idade:'))
    dicionário['idade'] = idade
    média += idade  
    lista.append(dicionário.copy())
    pergunta = '  '
    while pergunta not in 'sn':
        pergunta = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if pergunta == 'n':
        break
print('~'*22)
print(f'- O Grupo tem {len(lista)} pessoas')
print(f'- A média de idade é de {média / (len(lista)):.1f} anos.')
