'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
'''

#Resposta
soma_idades = 0
maior = 0
mulher_menor_de_vinte_anos = 0
n = 0
for c in range(0, 4):
    n = n + 1
    
    #Recebe o nome, idade e sexo da pessoa
    print(f'\n{n}°PESSOA')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').upper())

    #Caucula quantas mulheres com menos de 20 anos tem
    if sexo == 'F' and idade < 20 :
        mulher_menor_de_vinte_anos = mulher_menor_de_vinte_anos + 1

    #Calcula o nome do homem mais velho
    if idade > maior and sexo == 'M':
        maior = idade
        nome_do_mais_velho = nome
    
    #Calcula a media da idade de todas as pessoas 
    soma_idades += idade 

#Mostra quantas mulheres com menos de vinte anos tem
print(f'A quantidade de mulheres que tem menos de 20 anos e: {mulher_menor_de_vinte_anos}!!')

#Mostra o nome do homem mais velho
print(f'O nome do homem mais velho e: {nome_do_mais_velho}')

print(f'A media do grupo e: {soma_idades / 4}')