pessoas = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo  [F/M]: ')).upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('INVÁLIDO! DIGITE F OU M...')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:
        resposta = str(input('DESEJA CONTINUAR? S/N ?  ')).upper()[0]
        if resposta in 'SN':
            break
        print('TENTE NOVAMENTE COM S OU N...')
    if resposta == 'N':
        break
print(f'Temos {len(pessoas)} pessoas cadastradas.')
média = soma / len(pessoas)
print(f'A média de idade das pessoas é de {média:2.0f} anos.')
print('Mulheres cadastradas: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end= '')
print()
print('Pessoas acima da média: ', end='')
for p in pessoas:
    if p['idade'] >= média:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()