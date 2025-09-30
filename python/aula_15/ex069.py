'''
 Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
 o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
'''

cont_maioridade = 0 
cont_homens = 0
cont_mulheres_menor20 = 0
continuar = 'S'
while continuar == 'S':
    idade = int(input('Qual é a sua idade? '))
    sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        cont_maioridade += 1
    
    if sexo == 'F':
        if idade <= 20:
            cont_mulheres_menor20 += 1
    else: 
        cont_homens += 1


    continuar = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]

print(f'Tem {cont_maioridade} pessoas com mais de 18 anos')
print(f'Foram cadastrados {cont_homens} homens')
print(f'Tem {cont_mulheres_menor20} mulheres com menos de 20 anos')