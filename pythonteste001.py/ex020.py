import random

número1=str(input('primeiro aluno: '))
número2=str(input('Segundo aluno: '))
número3=str(input('terceiro aluno: '))
número4=str(input('quarto aluno: '))
lista=[número1,número2,número3,número4]
random.shuffle(lista)
print('a ordem de apresentação será ')
print(lista)