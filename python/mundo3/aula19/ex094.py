#Crie um programa que leia nome, sexo e idade de várias pessoas,guardando os dados
# de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

pessoa = []
soma_idade = 0
pessoa_acima_media = []
continuar = 'S'
while continuar == 'S':
  nome = input('Nome: ')
  sexo = input('Sexo [F/M]: ').upper()
  idade = int(input('Idade: '))
  pessoa_atual = {'nome': nome, 'sexo': sexo, 'idade': idade}
  pessoa.append(pessoa_atual)
  soma_idade += idade
  continuar = input('Você deseja cadastrar mais pessoas?[S/N] ').upper()
if len(pessoa) > 0:
    media_idade = soma_idade / len(pessoa)
else:
    media_idade = 0
print(f'{len(pessoa)} pessoas foram cadastradas.')
print(f'A média do grupo é: {media_idade:.2f}')
mulheres = []
for p in pessoa:
    if p['sexo'] == 'F':
        mulheres.append(p["nome"])
print(f'Lista de nomes de mulheres cadastradas: {mulheres}.')
for p in pessoa:
    if p['idade'] > media_idade:
        pessoa_acima_media.append(p['nome'])
print('As pessoas com idade acima da média são:')
for pessoa in pessoa_acima_media:
    print(f'{pessoa}')
