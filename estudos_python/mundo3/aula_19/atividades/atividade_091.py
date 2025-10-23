'''
 Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses 
 resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que 
 o vencedor tirou o maior número no dado.
'''

#Resposta
import random

dicionario_que_recebe_numeros_aleatorios = {}
for c in range(0, 6):
     numero_aleatorio = random.randint(1,6)
     
     
     