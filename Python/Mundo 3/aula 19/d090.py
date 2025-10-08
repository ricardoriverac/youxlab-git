sair = 'S'
situacao = []
nome = {}
media = {}
print('-'*26)
print('  DESCUBRA SE ESTÁ APROVADO OU REPROVADO:  ')
while sair == 'S':
    nome['Aluno'] = str(input('-> Nome do estudante: '))
    media['Média'] = int(input('-> Média do estudante: '))
    situacao.append(nome.copy())
    situacao.append(media.copy())
    sair = str(input('-> Escreva S para sair: '), end='\n').upper().strip()
    if sair == 'S':
        break
if media['Média'] < 7:
    print(f'-O Aluno {nome} está REPROVADO.')
else:
    print(f'-O Aluno {nome} está APROVADO.')
print('-'*26)
print('FINALIZANDO...')

