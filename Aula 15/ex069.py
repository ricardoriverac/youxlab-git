total18 = totalH = totalM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalH += 1
    if sexo == 'F' and idade < 20:
        totalM20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [s/n] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('Quantidade de pessoas maiores de 18: {}'.format(total18))
print('Contando podemos ter a conclusão de que temos {} homens cadastrados'.format(totalH))
print('e temos {} mulheres com menos de 20 anos'.format(totalM20))