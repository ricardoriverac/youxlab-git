#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
idade_homem_mais_velho = -1
nome_homem_mais_velho = ""
mulheres_menos_20 = 0
for i in range(0,4):
    print(f'Pessoa {i + 1}')
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()
    soma_idade += idade
    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
media_idade = soma_idade / 4
print(f"Média de idade do grupo: {media_idade:.2f}")
if nome_homem_mais_velho:
    print(f"Nome do homem mais velho: {nome_homem_mais_velho}")
else:
    print("Não houve homens cadastrados.")
print(f'Número de mulheres com menos de 20 anos: {mulheres_menos_20}')
