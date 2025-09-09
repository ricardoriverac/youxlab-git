import random
primeiroAluno = str(input('Digite o nome do primeiro aluno: '))
segundoAluno = str(input('Digite o nome do segundo aluno: '))
terceiroAluno = str(input('Digite o nome do terceiro aluno: '))
quartoAluno = str(input('Digite o nome do quarto aluno: '))
lista = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]
random.shuffle(lista)
print('[A sequência de apresentação será: ')
print (lista)

'''Segunda Forma:
from random import shuffle
primeiroAluno = str(input('Digite o nome do primeiro aluno: '))
segundoAluno = str(input('Digite o nome do segundo aluno: '))
terceiroAluno = str(input('Digite o nome do terceiro aluno: '))
quartoAluno = str(input('Digite o nome do quarto aluno: '))
lista = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]
shuffle(lista)
print('[A sequência de apresentação será: ')
print (lista)'''

'''Vídeo de exercício: https://youtu.be/OPh0nngbBSY?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6'''