#Cria um programa que leia o nome de uma cidade a diga sa ala começa ou não com o nome "SANTO".

#resposta

nome_cidade = input('Digite o nome da sua cidade: ')
print(nome_cidade[:5] == 'Santo')
