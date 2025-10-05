pessoa = dict()
pessoas = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:
        continuar = str(input('Dejesa continuar?[S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('Digite apenas S ou N')
    if continuar == 'N':
        break
print(f'ao todo são {len(pessoas)} pessoas cadastradas')
media = soma / len(pessoas)
print(f'a média de idades é {media:.0f}')
print('As mulheres cadastradas são ', end= '')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end= '')
print()
print('lista das pessoas acima da média: ')
for p in pessoas:
    if p['idade'] >= media:
        print(' ', end= '')
        for k, v in p.items():
            print(f'{k} = {v}; ', end= '')
        print()