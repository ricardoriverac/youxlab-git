from random import shuffle
a1 = str(input('aluno um: '))
a2 = str(input('aluno dois: '))
a3 = str(input('aluno tres: '))
a4 = str(input('aluno quatro: '))
lista  = [a1, a2, a3, a4 ]
shuffle (lista)
print ('a ordem de alunos é ')
print (lista)