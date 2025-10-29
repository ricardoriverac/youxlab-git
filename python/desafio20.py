from random import shuffle
num1 = str(input('primeiro aluno:'))
num2 = str(input('segundo aluno:'))
num3 = str(input('terceiro aluno:'))
num4 = str(input('quarto aluno:'))
lista = [num1, num2, num3, num4]
sorteio= shuffle(lista)
print(f'A ordem da lista será: {lista}')

