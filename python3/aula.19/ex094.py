dicionario = []
pessoa = {}
soma = contador = mulher = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Digite seu nome: '))
    while True:
        pessoa['Gênero'] = str(input('Digite seu gênero [M/F]: ')).strip().upper()[0]
        if pessoa['Gênero'] == 'F':
            mulher += 1
        if pessoa['Gênero'] in 'MF':
            break
        print('Erro! Digite apenas M, F .')
    pessoa['Idade'] = int(input('Digite sua idade: '))
    soma += pessoa['Idade']
    dicionario.append(pessoa.copy())
    while True:
        continuar = str(input('Desejas continuar? [S/N]: ')).upper()
        if continuar in 'SN':
            break
        print('Erro! Responda apenas com S ou N')
    if continuar == 'N':
        break
print('-='*30)
print(f'{len(dicionario)} pessoas foram cadastradas!')
print(f'A média de idade dessas pessoas é de {soma/len(dicionario):.2f} anos.')
if mulher > 1:
    print(f'Mulheres cadastradas = ', end='')
elif mulher == 1:
    print(f'O nome da mulher cadastrada é = ', end='')
else:
    print('Nenhuma mulher foi cadastrada')
for p in dicionario:
    contador += 1
    if p['Gênero'] == 'F':
        print(f'{p["Nome"]}, ', end='') if contador < len(dicionario) else print(f'{p["Nome"]}.')
print('Lista das pessoas com idade acima da média = ', end='')
contador = 0
for p in dicionario:
    contador += 1
    if p['Idade'] > (soma/len(dicionario)):
        print(f'{p["Nome"]}, ', end='') if contador < len(dicionario) else print(f'{p["Nome"]}.')
print(dicionario)     
print()   