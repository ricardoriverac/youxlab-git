# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

dados={''}
aluno=dict()

aluno['nome']=str(input('Nome: '))
aluno['média']=float(input(f'Média de {aluno["nome"]}: '))
   
print('-='*30)
if aluno['média'] >= 6:
    aluno['situação'] = 'Aprovado!'  
elif 5 <= aluno['média'] < 6:
    aluno['situação'] = 'Recuperação!'
else:
    aluno['situação'] = 'REPROVADO!!!!!!'

print(f'- O nome é {aluno["nome"]}')
print(f'- A média é {aluno["média"]}')
print(f'- O aluno foi {aluno["situação"]}')














