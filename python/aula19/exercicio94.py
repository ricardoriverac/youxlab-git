dic = {}
female = []
resp = ' '
soma = media = 0
while True:
    dic['pessoa'] = str(input('Nome: '))
    dic['sexo'] = str(input('Sexo: [M/F/N(Não Binário)/G(Gênero Flúido)]'))
    if dic['sexo'] not in 'MmFfNnGg':
        print('Não há opções no momento, sinto muito :(\nTente Novamente!')
    else:
        break
    if dic['sexo'] in 'Ff':
        female.append(dic.copy())
    dic['idade'] = int(input('Idade: '))
    soma += dic['idade']
    media = soma/len()
    