nome = input('Qual é o nome do aluno? ')
media = int(input('Qual é a média do aluno? '))

if media >= 7.0:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

aluno = { 
    'nome': nome,
    'media': media,
    'situacao': situacao
}

print(aluno)