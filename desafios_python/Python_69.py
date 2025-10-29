
totalpessoas = 0
maioresidade = 0
homens = 0
mulheresmenores20 = 0

while True:
    print('-=' * 30)
    print('CADASTRE UMA PESSOA')
    print('-=' * 30)

    idade = int(input('Idade: '))
    sexo = ''
    while sexo not in ['M', 'F']:
        sexo = str(input('Sexo [M/F]: ')).strip().upper()

    totalpessoas += 1
    if idade >= 18:
        maioresidade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresmenores20 += 1

    resposta = ''
    while resposta not in ['S', 'N']:
        resposta = str((input('Quer continuar? [S/N]: '))).strip().upper()

    if resposta == 'N':
        break

print('-=' * 30)
print('FIM DO PROGRAMA')
print(f'Total de pessoas cadastradas: {totalpessoas}')
print(f'Maiores de 18 anos: {maioresidade}')
print(f'Total de homens: {homens}')
print(f'Mulheres com menos de 20 anos: {mulheresmenores20}')
