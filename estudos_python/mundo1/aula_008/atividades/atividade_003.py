'''
Um professor quer sortear um dos seus quatro alunos para 
apagar o quadro. Faça um programa que ajuda ala, lando o 
nome dales a escrevendo o nome do escolhido.
'''

#Responde

import random

aluno1 = input('Digite o nome do primeiro aluno : ')
aluno2 = input('Digite o nome do segundo aluno :' )
aluno3 = input('Digite o nome do terceiro aluno : ')
aluno4 = input('Digite o nome do quarto aluno : ')
lista = [aluno1, aluno2 , aluno3, aluno4]
resultado = random.choices(lista)

print(f'O aluno escolhido foi {resultado}')