nota1 = float(input('Qual é a primeira nota? '))
nota2 = float(input('Qual é a segunda nota? '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a média do aluno é {media:.1f}')
if media >= 7:
    print('O aluno está APROVADO!')
elif 5 <= media < 7:
    print('O aluno está em RECUPERAÇÃO!')
else:
    print('O aluno está REPROVADO!')
