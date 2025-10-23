'''
Faça um programa que leia nome e média de um aluno, guardando também a 
situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''

#Resposta

dados_aluno = {}
nome = str(input('Digite o nome do aluno: '))
media = float(input('Digite a média do aluno: '))
print()
dados_aluno = {'Nome':nome , 'Media':media}
print(dados_aluno)

if media <= 4:
    dados_aluno['Situação_aluno'] = 'Reprovado'

elif media >= 4 and media < 7:
    dados_aluno['Situação_aluno'] = 'Recuperação'

elif media > 6:
    dados_aluno['Situação_aluno'] = 'Aprovado'

print(f'''
            DADOS DO ALUNO
      -=-=-=-=-=-=-=-=-=-=-=-=-=
      Nome do aluno: {dados_aluno["Nome"]}
      A média do aluno: {dados_aluno["Media"]}
      A situação do aluno: {dados_aluno["Situação_aluno"]} 


''')