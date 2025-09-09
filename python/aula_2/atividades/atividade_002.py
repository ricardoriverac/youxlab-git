'''
Faça um program que leia algo pelo teclado
e mostre na tela o seu tipo primitivo e todas
as informações possiveis sobre ele
'''

#Responda

informação_quaisquer = input('Digite quais quer coisa : ')

tipo_da_variavel = type(informação_quaisquer)
print(tipo_da_variavel)
print(informação_quaisquer.isnumeric())