#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.

lista = []
continua = 'S'
while continua == 'S':
    nome = input('Digite seu nome:')
    nota1 = float(input('Digite sua primeira nota: '))
    nota2 = float(input('Digite sua segunda nota: '))
    continua = input('Você deseja cadastrar mais pessoas?[S/N]').upper()
    media = (nota1 + nota2) / 2
    lista.append([nome,media])
print('-----BOLETIM-----')
print(*lista)

