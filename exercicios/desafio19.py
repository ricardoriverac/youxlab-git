import random
aluno1 = input('Qual o nome do primeiro aluno? ')
aluno2 = input('Qual o nome do segundo aluno? ')
aluno3 = input('QUal o nome do terceiro aluno? ')
aluno4 = input('Qual o nome do quarto aluno? ')
grupo = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(grupo)
print ('o aluno escolhido é {}'.format(escolhido))
