# listapessoas = []
# dicionario = {}
# mulheres = []
# mediamulheres = []
# soma = 0
# continuar = 'S/N'
# while continuar == 'S/N':
#      dicionario['nome'] = str(input('nome:'))
#      dicionario['sexo'] = str(input('sexo:[F/M]: ')).upper().strip()
#      dicionario['idade'] = int(input('idade:'))
#      listapessoas.append(dicionario) 
#      dicionario.copy()
#      continuar = str(input('quer continuar?[S/N]')).upper().strip()
#      while continuar not in 'SN':
#         print('ERRO.Digite apenas S e N')
#         continuar = str(input('quer continuar?[S/N]')).upper().strip()
# for l in listapessoas:
#     soma = sum(dicionario['idade'])
#     numeros = len(dicionario['idade'])
#     media = soma / numeros
#     media.append(dicionario['idade'])
#     if dicionario['sexo'] in 'F':
#         mulheres.append(dicionario['nome'])
# print(f'a media de idades e: {media}')
# print(f'as mulheres cadastradas sao: {mulheres}')
# print(F'as idades acima foram: {mediamulheres}')
# print(f'foram cadastradas {len(listapessoas)} pessoas')


listapessoas = []        
mulheres = []             
idades_acima_media = []   

# Loop principal de cadastro
while True:
    dicionario = {}  # Cria um novo dicionário a cada laço (senão, reescreve o mesmo)
    
    dicionario['nome'] = input('Nome: ')
    
    # Entrada do sexo com validação
    while True:
        sexo = input('Sexo [F/M]: ').strip().upper()
        if sexo in ['F', 'M']:
            dicionario['sexo'] = sexo
            break
        else:
            print('ERRO! Digite apenas F ou M.')
    
    # Entrada da idade
    dicionario['idade'] = int(input('Idade: '))
    
    # Soma a idade para média posterior
    soma_idades += dicionario['idade']
    
    # Adiciona dicionário copiado à lista
    listapessoas.append(dicionario.copy())
    
    # Verifica se deve continuar
    while True:
        continuar = input('Quer continuar? [S/N]: ').strip().upper()
        if continuar in ['S/N']:
            break
        else:
            print('ERRO! Digite apenas S ou N.')
    
    if continuar == 'N':
        break

# Cálculo da média de idade
total_pessoas = len(listapessoas)
media_idade = soma_idades / total_pessoas

# Preenchimento das listas de mulheres e de pessoas acima da média
for pessoa in listapessoas:
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    if pessoa['idade'] > media_idade:
        idades_acima_media.append(pessoa)

# Exibição dos resultados
print(' RESULTADOS')
print(f'Total de pessoas cadastradas: {total_pessoas}')
print(f'Média de idade: {media_idade:.2f} anos')
print(f'Mulheres cadastradas: {mulheres}')

print(f' Pessoas com idade acima da média:')
for p in idades_acima_media:
    print(f" {p['nome']} ({p['idade']} anos)")
