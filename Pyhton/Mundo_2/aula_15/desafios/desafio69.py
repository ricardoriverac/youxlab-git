anos18 = homens = mulher20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo?: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        anos18 = anos18 + 1
    if sexo == 'M':
        homens = homens + 1
    if sexo == 'F' and idade < 20:
        mulher20 = mulher20 + 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Você quer continuar?: [s/n] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Tem {anos18} pessoas com mais de 18 anos.')
print(f'No total temos {homens} homens cadastrados')
print(f'Temos também {mulher20} mulheres com menos de 20 anos')