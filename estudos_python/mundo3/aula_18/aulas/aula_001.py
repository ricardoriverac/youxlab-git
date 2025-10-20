'''
Crie um programa que:

Peça o nome e a idade de duas pessoas.
Guarde essas informações dentro de uma lista composta (ou seja, uma lista que contém outras listas).
Mostre no final o nome e a idade de cada pessoa cadastrada.
'''

#Resposta
lista = list()
nome = str(input('Digite um nome: '))
idade = str(input('Digite a idade: '))

lista1 = list()
lista1.append(nome)
lista1.append(idade)


nome = str(input('Digite um nome: '))
idade = str(input('Digite a idade: '))

lista2 = list()
lista2.append(nome)
lista2.append(idade)
lista.append(lista2)
lista.append(lista1)
print(lista)