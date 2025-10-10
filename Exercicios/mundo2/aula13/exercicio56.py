soma_de_idades=0
idade_homem_mais_velho= 0
nome_homem_mais_velho=""
quantidade_mulheres=0

for dados in range(4):
    nome = str(input(f"Digite o nome da {dados+1}ª pessoa: "))
    idade = int(input(f"Digite a idade da {dados+1}ª pessoa: "))
    sexo = str(input(f"Digite o sexo da {dados+1}ª pessoa [M ou F]: ")).upper()
    soma_de_idades += idade
    # soma_de_idades = soma_de_idades + idade
    if  sexo == "M" and idade >  idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    
    if sexo =="F" and idade < 20 :
        quantidade_mulheres += 1 


media=soma_de_idades/4
print(f"A media de idades é {media}")
print(f"O nome do homem mais velho é : {nome_homem_mais_velho}")
print(f" Ha {quantidade_mulheres} mulheres menores de vinte anos")

    