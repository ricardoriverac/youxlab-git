from random import choice

número1=str(input('Primeiro aluno: '))
número2=str(input('Segundo aluno: '))
número3=str(input('Terceiro aluno:'))
número4=str(input('quarto aluno: '))
lista=[número1,número2,número3,número4]
escolhido=choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))
