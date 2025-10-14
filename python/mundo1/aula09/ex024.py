#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o
#nome "SANTO".

city = str(input('Qual cidade você nasceu? '))
print(city[0:5] == 'Santo')