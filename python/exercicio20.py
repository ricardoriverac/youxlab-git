import random
a1 = input('aluno um: ')
a2 = input('aluno dois: ')
a3 = input('aluno tres: ')
a4 = input('aluno quatro: ')
lista  = [a1, a2, a3, a4 ]
random.shuffle (lista)
print ('a ordem de alunos é ')
print (lista)