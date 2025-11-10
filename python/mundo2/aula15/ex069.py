# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

pessoas_mais_18 = 0
homens_cadastrados = 0
mulheres_20 = 0
continuar = 'S'
while continuar == 'S':
    idade = int(input('Quantos anos você tem ->'))
    sexo = input('Qual é seu sexo:[M/F]').strip().upper()
    while sexo not in 'MF':
      sexo = input('Sexo inválido digite "M ou F" para validar o sexo')
    if idade >= 18:
        pessoas_mais_18 += 1
    if sexo == 'M':
        homens_cadastrados += 1
    if sexo == 'F' and idade < 20:
        mulheres_20 += 1
    continuar = input('Você deseja continuar? [S/N]: ').upper()
print(f'Tem {pessoas_mais_18} pessoas maior de 18 anos.')
print(f'{homens_cadastrados} homem foi cadastrado.')
print(f'{mulheres_20} mulher tem menos de 20 anos.')



