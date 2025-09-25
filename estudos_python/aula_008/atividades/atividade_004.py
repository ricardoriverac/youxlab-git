'''
O mesmo professor do desafio anterior quer sortear a ordem da 
apresentação de trabalhos dos alunos. Faça um programa que leia 
o nome dos quatro alunos a mostra a ordem sorteada.
'''

#Resultado

import random

aluno1 = input('Digite o nome do primeiro aluno : ')
aluno2 = input('Digite o nome do segundo aluno :' )
aluno3 = input('Digite o nome do terceiro aluno : ')
aluno4 = input('Digite o nome do quarto aluno : ')
lista = [aluno1, aluno2 , aluno3, aluno4]
resultado = random.shuffle(lista)

print(f'A sequancia de alunos que irão apresentar é: ')
print(lista)
