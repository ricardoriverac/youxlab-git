from random import choice
numero1 = str(input('Primeiro aluno:'))
numero2 = str(input('Segundo aluno:'))
numero3 = str(input('Terceiro aluno:'))
numero4 = str(input('Quarto aluno:'))
lista = [numero1,numero2,numero3,numero4]
escolhido = choice(lista)
print('O aluno escolhido foi {}' .format(escolhido))
