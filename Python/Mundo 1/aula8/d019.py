from random import choice
pessoa1 = input('Primeiro aluno: ')
pessoa2 = input('Segundo auno: ')
pessoa3 = input('Terceiro aluno: ')
pessoa4 = input('Quarto aluno: ') 
lista = [pessoa1, pessoa2, pessoa3, pessoa4]
escolhido = choice(lista)
print('O aluno escolhido foi: {} '.format(escolhido))