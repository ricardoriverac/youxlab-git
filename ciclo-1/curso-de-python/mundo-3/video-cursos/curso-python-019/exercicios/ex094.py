cadastroLista = []
maiorIdade = []
mulheres = []
cadastro = {}

countIdade = 0
countPessoas = 0


while True:
    cadastro['nome'] = str(input('Digite seu nome: '))
    cadastro['sexo'] = str(input('Digite seu sexo: [M/F] ')).upper()

    if cadastro['sexo'] not in 'MF':
        break
    if cadastro['sexo'] == 'F':
        mulheres.append(cadastro["nome"])

    cadastro['idade'] = int(input('Digite sua idade: '))
    countIdade += cadastro['idade']
    countPessoas += 1

    media = countIdade / countPessoas

    if cadastro['idade'] >= media:
        maiorIdade.append(cadastro.copy())

    cadastroLista.append(cadastro.copy())


    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

print('-' * 25)

print(f'Foram cadastrados \033[33m{len(cadastroLista)}\033[m pessoas.')
print(f'A média de idade das pessoas é \033[33m{media:.0f}\033[m')

print(f'As mulheres cadastradas são: ')
for m in mulheres:
    print(f'-{m}')

print('-' * 25)

print('As pessoas maiores de que a média são:')

for p in maiorIdade:
    for k, v in p.items():
            print(f' {k} = {v};')