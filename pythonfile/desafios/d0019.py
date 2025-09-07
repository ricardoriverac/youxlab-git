import random
aluno = str(input(' Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
lista = [aluno, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))