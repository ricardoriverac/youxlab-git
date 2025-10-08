'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor Correto.
'''

#Resposta
digite_sexo = 'r'


while digite_sexo not in 'MF':
    digite_sexo = str(input('Digite o sexo da pessoa: ').upper())
    print('oi')

