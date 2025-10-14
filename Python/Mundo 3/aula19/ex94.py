# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em
#  um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = []
somaIdades = 0
mulheres = []
maiorIdade = []

while True:
    nome = input('Nome: ')
    sexo = input('Sexo (M/F): ').upper()
    idade = int(input('Idade: '))

    pessoa = {'nome': nome, 'sexo': sexo, 'idade': idade}
    pessoas.append(pessoa)

    somaIdades += idade

    if sexo == 'F':
        mulheres.append(pessoa)

    if input('Deseja continuar? (S/N) ')[0] in 'n':
        break
print('-'*50)
totalCadastrados = len(pessoas)
print(f'Total de pessoas cadastradas: {totalCadastrados}')

mediaIdade = somaIdades / totalCadastrados
print(f'Média de idade: {mediaIdade:.2f} anos')

print('Mulheres cadastradas:')
for p in mulheres:
    print(f'{p["nome"]}')
print('Pessoas com idade acima da média:')
for p in pessoas:
    if p['idade'] > mediaIdade:
        maiorIdade.append(p)
        print(f'  Nome: {p["nome"]}, Idade: {p["idade"]}, Sexo: {p["sexo"]}')