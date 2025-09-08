import random
aluno = str(input(' Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
lista = [aluno, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem de apresentação sera: ')
print(lista)