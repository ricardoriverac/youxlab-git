#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo sem considerar espaços.
#Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))
nome_maiu = nome.upper()
print(f'Seu nome em letras maiúsculas é: {nome_maiu}')
nome_minus = nome.lower()
print(f'Seu nome em letras minúsculas é: {nome_minus}')
nome_espaco = nome.replace(" ", " ")
number_let = len(nome_espaco) - nome.count(" ")
print(f'O nome sem contar espaço tem {number_let} letras')
primeiro_nome = nome.split()[0]
quantidade_letras = len(primeiro_nome)
print(f'A quantidae de letras no primeiro nome é: {quantidade_letras}')