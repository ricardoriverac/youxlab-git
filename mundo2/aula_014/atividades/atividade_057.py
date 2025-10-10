'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor Correto.
'''

#Resposta

digite_sexo = 'r'
digite_sexo = str(input('Digite o sexo da pessoa[m/f]: '))
while digite_sexo not in 'MFmf':
    digite_sexo = str(input('Dados inválidos. Digite novamente: '))

if digite_sexo == 'M' or digite_sexo == 'm':
    print('O seu sexo e MASCULINO!!')

elif digite_sexo == 'F' or digite_sexo == 'f':
    print('O seu sexo e FEMININO!!')

