import random
numero1 = str(input('Qual è o primeiro aluno? '))
numero2 = str(input('Qual é o segundo aluno? '))
numero3 = str(input('Qual é o terceiro aluno? '))
numero4 = str(input('Qual é o terceiro aluno? '))
lista = [numero1, numero2, numero3, numero4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')