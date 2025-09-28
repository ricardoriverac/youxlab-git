from random import choice
alunoUm = str(input('Digite o nome do primeiro aluno: '))
alunoDois = str(input('Digite o nome do segundo aluno: '))
alunoTres = str(input('Digite o nome do terceiro aluno: '))
alunoQuatro = str(input('Digite o nome do quarto aluno: '))
lista = [alunoUm, alunoDois, alunoTres, alunoQuatro]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))