'''
Faça um program que leia algo pelo teclado
e mostre na tela o seu tipo primitivo e todas
as informações possiveis sobre ele
'''

#Responda

informação_quaisquer = input('Digite quais quer coisa : ')

tipo_da_variavel = type(informação_quaisquer)

print(f'O tipo primitivo é {tipo_da_variavel}')
print('E um número : ' , informação_quaisquer.isnumeric())
print('E uma palavra ou letra : ' , informação_quaisquer.isalpha())
print('Esta em maiusculo : ' , informação_quaisquer.isupper())
print('Esta em minusculo : ' , informação_quaisquer.islower())
print('Contem letras e números : ' , informação_quaisquer.isalnum())
print('Esta captalizada : ' , informação_quaisquer.istitle())
print('Contem somente espeço : ' , informação_quaisquer.isspace())