continuar = 'S'
dadosPessoas = {}
pessoas = []
qtdPessoas = 0
idades = []
mulheres = []
idadesMaiorMedia = []
print('-'*40)
print('   UNINDO DICIONÁRIOS E LISTAS   ')
print('-'*40)
while continuar == 'S':
    dadosPessoas['nome'] = str(input('-> Nome: '))
    qtdPessoas += 1
    dadosPessoas['sexo'] = str(input('-> Sexo: [M/F]: ')).upper().strip()
    dadosPessoas['idade'] = int(input('-> Idade: '))
    idades.append(dadosPessoas["idade"])
    pessoas.append(dadosPessoas['nome'])
    pessoas.append(dadosPessoas['sexo'])
    pessoas.append(dadosPessoas['idade'])
    if dadosPessoas['sexo'] == 'F':
        mulheres.append(dadosPessoas['nome'])
    mediaIdade = sum(idades) / qtdPessoas
    if dadosPessoas['idade'] > mediaIdade:
        idadesMaiorMedia.append(idades)
    print('-'*40)
    continuar = str(input(('-> Deseja continuar? [S/N]: '))).upper().strip()
    print('-'*40)
    if continuar == 'N':
        print('=-'*20)
        print('   DADOS FINAIS   ')
        print('=-'*20)
        print(f'-Foram cadastradas: {qtdPessoas} pessoas.\n-A média de idade é: {mediaIdade} anos.\n-Lista de mulheres: {mulheres}.\n-Lista de idades acima da média: {idades}.')
        print('-'*40)
        print('FINALIZANDO...')
        print('-'*40)
