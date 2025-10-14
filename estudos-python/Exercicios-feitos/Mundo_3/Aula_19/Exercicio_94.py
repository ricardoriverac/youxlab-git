pessoas = []
dados = {}
mulheres = []
soma = 0
acimaDaMedia = []
while True:
    dados['nome'] = str(input('Coloque o seu nome:\n->').capitalize())
    dados['sexo'] = str(input('Coloque o seu sexo:\n[H] para homens e [M] para mulheres\n->').strip().upper())
    if dados['sexo'] == 'M':
        mulheres.append(dados.copy())
    idade = int(input('Coloque a sua idade:\n->'))
    soma += idade
    dados['idade'] = idade
    pessoas.append(dados.copy())
    opcao = str(input('Você quer adicionar mais alguem?\nSe quiser continuar escreva qualquer coisa\nSe não, escreva "N" ou "n"!\n->')).strip().upper()
    if opcao == 'N':
        break
media = soma/len(pessoas)
print (f'{len(pessoas)} pessoas foram cadastradas!')
print(f'A média de idade foi de {media:.2f} anos')
if len(mulheres) > 0:
    print (f'{len(mulheres)} mulheres foram cadastradas!')
else:
    print ('Não foram cadastradas mulheres')
for p in pessoas:
    if p['idade'] > media:
        acimaDaMedia.append(p['nome'])
print (f'{acimaDaMedia} são as pessoas que estão acima da média de idade!')