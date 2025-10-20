listapeso = []
resposta = 'S'
dados_pessoa = []
while resposta == 'S':
    nome = str(input(f'NOME: '))
    peso = int(input(f'PESO: '))
    dados_pessoa.append(nome)
    dados_pessoa.append(peso)
    listapeso.append(dados_pessoa)
    resposta = str(input(f'deseja continuar? [S/N]')).upper()

print(f'o maior peso foi {peso}')
print(f'o menor peso foi {peso}')
print(f'total de pessoas cadastradas {len(listapeso)}')

