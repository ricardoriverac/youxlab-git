'''
Faça um programa que leia o nome completo de uma pessoa.
mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
'''

#Resposta
digite_o_seu_nome = input('Digite o seu nome: ')
n = (digite_o_seu_nome.split())
ultimo_nome = (n[len(n)-1])

print(f'O primeiro nome: {n[0]}')
print(f'O ultimo nome: {ultimo_nome}')