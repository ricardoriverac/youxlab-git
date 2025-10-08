print('\033[033m''ANÁLISE DE DADOS\033[m')

homem_maisvelho = 0
nome_maisvelho = ''
soma_idade = 0
qtde_mulheres_menores_20 = 0

for cont in range(1,5):
    print('='*20)
    print(f'{cont}º Pessoa')
    print('='*20)
    nome = str(input(f'Digite o nome: ')).strip().upper()
    idade = int(input(f'Digite a idade: '))
    sexo = str(input(f'Digite o sexo: [M] ou [F]: ')).strip().upper()
    soma_idade += idade
    if sexo[0] == 'M':
        if idade > homem_maisvelho:
            homem_maisvelho = idade
            nome_maisvelho = nome
        else:
            homem_maisvelho = homem_maisvelho
            nome_maisvelho = nome_maisvelho
    if sexo[0] == 'F' and idade < 20:
        qtde_mulheres_menores_20 += 1

print('=-'*30)
media_idade = soma_idade/4
print(f'A media da idades das {cont} pessoas é: {media_idade} anos')
print(f'A idade do homem mais velho é {homem_maisvelho} anos e seu nome é {nome_maisvelho}')
if qtde_mulheres_menores_20 <= 1:
    print(f'{qtde_mulheres_menores_20} mulher tem menos de 20 anos.')
else:
    print(f'{qtde_mulheres_menores_20} mulheres tem menos de 20 anos')