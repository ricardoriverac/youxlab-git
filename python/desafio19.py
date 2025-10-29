import random

('impot random')
num1 = str(input('primeiro aluno:'))
num2 = str(input('segundo aluno'))
num3 = str(input('treceiro aluno'))
num4 = str(input('quarto aluno'))
lista = [num1, num2, num3, num4]
escolhido = random.choice(lista)
print(f'o escolhido foi:{escolhido}')