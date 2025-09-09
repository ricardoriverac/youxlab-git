import random
alunoUm = str(input('Digite o nome do primeiro aluno: '))
alunoDois = str(input('Digite o nome do segundo aluno: '))
alunoTres = str(input('Digite o nome do terceiro aluno: '))
alunoQuatro = str(input('Digite o nome do quarto aluno: '))
lista = [alunoUm, alunoDois, alunoTres, alunoQuatro]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

'''Segunda Forma
from random import choice
alunoUm = str(input('Digite o nome do primeiro aluno: '))
alunoDois = str(input('Digite o nome do segundo aluno: '))
alunoTres = str(input('Digite o nome do terceiro aluno: '))
alunoQuatro = str(input('Digite o nome do quarto aluno: '))
lista = [alunoUm, alunoDois, alunoTres, alunoQuatro]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))'''

'''Vídeo de exeercício: https://youtu.be/_Nk02-mfB5I?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6'''