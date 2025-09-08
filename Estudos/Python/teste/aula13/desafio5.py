import random
aluno1= str (input('Qual o nome do aluno? '))
aluno2= str(input('Qual o nome do aluno? '))
aluno3= str(input('Qual o nome do aluno? '))
aluno4= str(input('Qual o nome do aluno? '))
print(aluno1)
print(aluno2)
print(aluno3)
print(aluno4)

ordenação= random.shuffle([aluno1, aluno2, aluno3, aluno4], 4) 
print(f'A nova ordem dos alunos é: {ordenação}')
