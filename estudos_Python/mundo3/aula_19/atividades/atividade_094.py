'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de 
cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 

A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

#Resposta
idade_maior_media = []
mulheres = []
soma_media = []
contador = 0

#Fica perguntando o nome, sexo e a idade de varias pessoas
while True:
    dados = {'Nome':str(input('\nDigite o nome: ')) , 'Idade':int(input('Digite a idade: ')) , 'Sexo':str(input('Digite o sexo[m/f]: ')).lower()}
    contador += 1
    continuar = str(input('Quer continuar[s/n]: ')).lower()

    soma_media.append(dados['Idade'])

    if dados['Sexo'] == 'f':
        mulheres.append(dados['Nome'])
 
    if dados['Idade'] > sum(soma_media) / contador:
        idade_maior_media.append(dados['Nome'])

    if continuar == 'n':
        break

print(f'\nA quantidade de pessoas cadastradas foi: {contador}')
print(f'A média das idades somadas e {sum(soma_media) / contador}')
print(f'A lista com somente as mulheres: {mulheres}')
print(f'Uma lista com as pessoas com a idade acima da média: {idade_maior_media}')