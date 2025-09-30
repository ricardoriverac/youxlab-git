while True:
    print('-'*20, '\nCADASTRE UMA PESSOA:')
    idade = int(input('Idade: '))
    sexo = ' '
    continuar = ' '
    countM = countF = countGeral = 0
    if idade >= 18:
        countGeral += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        print('-'*20)
    if sexo in 'F' and idade <= 20:
        countF += 1
    if sexo in 'M':
        countM += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'S':
        print('-'*20)
    else:
        print('-'*20)
        break
print(f'''Existem [ {countGeral} ] maiores de 18 anos
      Existem [ {countF} ] mulheres menores de 20 anos
      Existem [ {countM} ] homens''')
        