listaPessoas = []  # Lista principal que vai guardar os dicionários com os dados de cada pessoa

while True:
    nome = str(input('Nome: '))  # Lê o nome da pessoa
    sexo = str(input('Sexo: ')).strip().upper()[0]  # Lê o sexo (apenas a primeira letra, em maiúscula)

    while sexo != 'M' and sexo != 'F':  # aceita apenas 'M' ou 'F'
        print('Digite um sexo válido!')
        sexo = str(input('Sexo: ')).strip().upper()[0]

    idade = int(input('Idade: '))  # Lê a idade da pessoa

    while idade < 0:  # garante que a idade não é negativa
        print('Digite uma idade válida!')
        idade = int(input('Idade:'))

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]  # Pergunta se quer continuar

    while resposta not in 'SN':  # Validação da resposta
        print('Digite uma resposta válida!')
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    print()  # pula uma linha

    pessoa = dict()  # Cria um dicionário para armazenar os dados da pessoa atual
    pessoa['nome'] = nome  # Adiciona o nome ao dicionário
    pessoa['sexo'] = sexo  # Adiciona o sexo ao dicionário
    pessoa['idade'] = idade  # Adiciona a idade ao dicionário

    listaPessoas.append(pessoa)  # Adiciona o dicionário à lista principal

    if resposta == 'N':  # Se a resposta for "N", o laço para e encerra o cadastro
        break

print(listaPessoas)  # Mostra a lista completa de dicionários cadastrados

print(f'- O grupo tem {len(listaPessoas)} pessoas.')  # Mostra o total de pessoas cadastradas

somaIdades = 0
mediaIdade = 0
for i in range(0, len(listaPessoas)):  # Percorre a lista para somar as idades
    somaIdades += listaPessoas[i]['idade']
    mediaIdade = somaIdades / (i + 1)  # Calcula a média a cada passo (poderia ser fora do laço)

print(f'- A média de idade é de {mediaIdade:.2f} anos.')  # Mostra a média de idade com duas casas decimais

print(f'- As mulheres cadastradas foram: ', end='')  # Inicia a listagem das mulheres
for i in range(0, len(listaPessoas)):  # Percorre a lista
    if listaPessoas[i]['sexo'] == 'F':  # Se o sexo for feminino, mostra o nome
        print(listaPessoas[i]['nome'], end='; ')
print()  # Pula linha

print('- Lista de pessoas que estão acima da média: ')  # Título da lista de quem tem idade acima da média
for i in range(0, len(listaPessoas)):  # Percorre a lista
    if listaPessoas[i]['idade'] > mediaIdade:  # Se a idade for maior que a média
        print(f'nome = {listaPessoas[i]["nome"]}; sexo = {listaPessoas[i]["sexo"]}; idade = {listaPessoas[i]["idade"]};')
        print()  # Linha em branco para separar visualmente os registros
