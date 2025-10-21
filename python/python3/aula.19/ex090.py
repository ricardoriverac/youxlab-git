situacao = []
nome = {}
media = {}

while True:
    nome['Aluno:'] = str(input('Digite o nome do aluno '))
    media['Média'] = float(input('Digite a média do aluno '))
    if media['Média'] >= 7:
        print(f'Aluno {nome} aprovado')
    else:
        print(f'Aluno {nome} reprovado')
    situacao.append(nome.copy())
    situacao.append(media.copy())
    break